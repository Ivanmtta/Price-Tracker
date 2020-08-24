import React, {useState, useEffect} from 'react';
import {Item} from './Item'

const  API = process.env.REACT_APP_API;

export const PageContent = (props)=>{

  const [link, setLink] = useState('');
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);

  const createItem = async (event)=>{
    if(link === '') return;
    setLoading(true);
    setLink('');
    await fetch(API + 'items', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "url": link
      })
    });
    await getItems();
    setLoading(false);
  }

  const getItems = async ()=>{
    const response = await fetch(API + 'items');
    const data = await response.json();
    setItems(data);
  }

  const deleteItem = async (id)=>{
    if(!window.confirm('Are you sure wou want to delete it?')){
      return;
    }
    await fetch(API + 'delete/' + id, {
      method: 'DELETE'
    });
    await getItems();
  }

  useEffect(()=>{
    getItems();
  }, []);

  return (
    <div className="row">
      <div className="col-md-5 mb-4">
        <div className="card bg-secondary">
          <div className="card-body">
            <div className="form-group">
              <div className="custom-text-input">
                <input 
                id="text-input" 
                className="custom-text" 
                type="text" 
                onChange={event => setLink(event.target.value)}
                value={link}
                autoComplete="off"
                />
                <label className="custom-label" htmlFor="text-input">Amazon Link</label>
              </div>
              <input 
                type="button" 
                className="custom-button mt-4 float-right" 
                value="ADD ITEM"
                onClick={createItem}
              />
            </div>
          </div> 
        </div>
      </div>
      <div className="col-md-7">
        {items.map((item)=>
          <Item 
            key={item._id}
            id={item._id}
            name={item.name}
            image={item.image}
            url={item.url}
            original_price={item.original_price}
            current_price={item.current_price}
            delete={deleteItem}
          />
        )}
        {loading &&
          <div className="text-center">
          <div className="spinner-grow"></div>
          <div className="spinner-grow"></div>
          <div className="spinner-grow"></div>
          <div className="spinner-grow"></div>
          <div className="spinner-grow"></div>
        </div>
        }
      </div>
    </div>
  );
}