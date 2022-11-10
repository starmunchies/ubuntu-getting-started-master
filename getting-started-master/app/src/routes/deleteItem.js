const db = require('../persistence');

module.exports = async (req, res) => {
    if(!process.env.READ)
    {
    await db.removeItem(req.params.id);
    }
    
    res.sendStatus(200);
};
