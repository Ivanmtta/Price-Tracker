import React from 'react';

import {FaTrashAlt} from 'react-icons/fa';

export const Item = (props)=>{

  return (
    <div className="card bg-secondary mb-4 a">
      <div className="card-body">
        <div className="row">
          <div className="col-3 d-flex justify-content-center align-items-center">
            <img alt='' className="img-fluid" src={props.image} width="150rem" height="150rem" />
          </div>
          <div className="col-9">
            <div className="row justify-content-end p-2">
              <button 
                className="icon-button" 
                onClick={()=>props.delete(props.id)}><FaTrashAlt 
                size="1.4rem"/></button>
            </div>
            <div className="row">
              <h4 className="card-title">
                {props.name}
              </h4>
            </div>
            <div className="row">
              <div className="col-6 p-0">
                <p>Original Price: ${props.original_price}</p>
              </div>
              <div className="col-6 p-0">
                <p>Current Price: ${props.current_price}</p>
              </div>
            </div>
            <div className="row justify-content-end pr-4">
              <form action={props.url} target="_blank">
                <input type="submit" className="custom-button mt-4" value="PRODUCT LINK" data-toggle="tooltip" data-placement="top" title="Tooltip on top"/>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}