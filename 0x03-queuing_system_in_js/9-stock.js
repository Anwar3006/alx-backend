const express = require('express')
const app = express()
const client = require('redis').createClient()
const { promisify } = require('util');
const PORT = process.env.PORT || 1245

const listProducts = [
    {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
    {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
    {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
    {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5}
]

// Promisify Redis commands
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const getItemById = (id) => {
    return listProducts.find((product) => product.itemId === id)
}

const reserveStockById = async (itemId, stock) => {
    const key = `item.${itemId}`
    await setAsync(key, stock)
}

const getCurrentReservedStockById = async (itemId) => {
    try {
        const key = `item.${itemId}`
        const reservedStock = await getAsync(key)
        return reservedStock
    } catch (error) {
        console.error('Error: ', error);
    } finally {
        client.quit()
    }
}
//middleware to parse json
app.use(express.json())

// routes
app.get('/list_products', (req, res) => {
    res.status(200).json(listProducts)
})

app.get('/list_products/:itemId', (req, res) => {
    const { itemId } = req.params
    // console.log(itemId);
    const product = getItemById(Number(itemId))
    if (product){
        getCurrentReservedStockById(itemId)
        .then((result) => Number.parseInt(result || 0))
        .then((reservedStock) => {
            product.currentQuantity = product.initialAvailableQuantity - reservedStock
            res.status(200).json(product)
        })
    }else {
        res.json({"status":"Product not found"})
    }
})

app.get('/reserve_product/:itemId', (req, res) => {
    const {itemId} = req.params;
    const productItem = getItemById(parseInt(itemId));
  
    if (!productItem) {
      res.json({ status: 'Product not found' });
      return;
    }
    getCurrentReservedStockById(itemId)
        .then((result) => Number.parseInt(result || 0))
        .then((reservedStock) => {
            if (reservedStock >= productItem.initialAvailableQuantity) {
                return res.json(
                    {"status":"Not enough stock available", itemId}
                )
            }
        reserveStockById(itemId, reservedStock + 1)
            .then(() => {
            res.json({ status: 'Reservation confirmed', itemId });
        });
    })
})

app.listen(PORT, () => {
    try {
        //connect to redis
        client.on('connect', () => {
            console.log('Redis client connected to server');
        })
        console.log(`Server started, listening on port: ${PORT}...`);
    } catch (error) {
        console.error(error);
    }
})

export default app;