import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [items, setItems] = useState([]);
    const [newItem, setNewItem] = useState('');

    useEffect(() => {
        axios.get('/api/items').then(res => setItems(res.data));
    }, []);

    const addItem = () => {
        axios.post('/api/items', { item: newItem }).then(() => {
            axios.get('/api/items').then(res => setItems(res.data));
            setNewItem('');
        });
    };

    return (
        <div>
            <h1>Items</h1>
            <input value={newItem} onChange={e => setNewItem(e.target.value)} />
            <button onClick={addItem}>Add</button>
            <ul>{items.map(item => <li key={item}>{item}</li>)}</ul>
        </div>
    );
}

export default App;