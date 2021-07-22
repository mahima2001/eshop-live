import React,{useState,useEffect} from 'react'
import {Row,Col} from 'react-bootstrap'
import Product from '../components/Product'
import { useDispatch, useSelector } from 'react-redux'; //useSelector to get specific part of our state
import { listProducts } from '../actions/productActions'
import Loader from '../components/Loader'
function Homescreen() {
    const dispatch=useDispatch()
    const productList=useSelector(state =>state.productList) // we are pulling out the productlist part of reducer; do see in store; it has other parts like loading and error
    const {error,loading, products}=productList
    useEffect(()=>{       //IT gets triggered when the component loads or some state changes

        
        dispatch(listProducts())
        
        
    },[dispatch])//We are using [] at the end so that it only gets triggered when components loads

    return (
        <div>
            <h1>Latest products</h1>
            {loading?<Loader/>
            :  error? <h3>{error}</h3>
            :
            <Row>
                {products && products.map(product =>(
                    <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                    <Product product={product}/>
                    </Col>
                )
                )
                
                }
            </Row>
}
        </div>
    )
}

export default Homescreen
