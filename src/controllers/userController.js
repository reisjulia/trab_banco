const User = require('../models/User');

exports.getAllUsers = async (req, res) => {
    try {
        const users = await User.find();
        res.status(200).json(users);
    } catch (error) {
        res.status(400).json({message: error.message})
    }
};

exports.createUser = async (req, res) => {
    const { username, email } = req.body;
    try {
        const newUser = new User({ username, email, password });
        await newUser.save();
        res.status(201).json(newUser);
    } catch (error) {
        res.status(400).json({message: error.message})
    }
};

exports.updateUser = async (req, res) => {
    const { id } = req.params;
    const { username, email, password } = req.body;
    try {
        const updatedUser = await User.findByIdAndUpdate(id, { username, email, password }, { new: true });
        if (!updatedUser) {
            return res.status(404).json({ message: "Usuário não encontrado, tente novamente" });
        }
        res.status(200).json(updatedUser);
    } catch (error) {
        res.status(400).json({message: error.message})
    }
};

exports.deleteUser = async (req, res) => {
    const { id } = req.params;
    try {
        const deletedUser = await User.findByIdAndDelete(id);
        if (!deletedUser) {
            return res.status(404).json({ message: "Usuário não encontrado, tente novamente" });
        }
        res.status(200).json({ message: "Usuário deletado" });
    } catch (error) {
        res.status(400).json({message: error.message})
    }
};

