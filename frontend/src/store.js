import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import { productListReducers,productDetailsReducer } from './reducers/productReducers'
import { cartReducer } from './reducers/cartReducers'
import { userLoginReducers, userRegisterReducer,userDetailsReducer,userUpdateProfileReducer } from './reducers/userReducers'
import { orderCreateReducer,orderDetailsReducer, orderPayReducer,orderListMyReducer,orderListReducer,orderDeliverReducer, } from './reducers/orderReducers'



const reducer=combineReducers({
  productList:productListReducers,
  productDetails:productDetailsReducer,
  
  cart:cartReducer,
  userLogin:userLoginReducers,
  userRegister:userRegisterReducer,
  userDetails:userDetailsReducer, 
  userUpdateProfile:userUpdateProfileReducer,

  orderCreate: orderCreateReducer,
    orderDetails: orderDetailsReducer,
    orderPay: orderPayReducer,
    orderListMy: orderListMyReducer,
    orderList: orderListReducer,
    orderDeliver: orderDeliverReducer,
  
})

const cartItemsfromlocalStorage= localStorage.getItem('cartItems')
        ? JSON.parse(localStorage.getItem('cartItems'))
        : []//Items don't exist

const userInfoFromStorage = localStorage.getItem('userInfo') ?
        JSON.parse(localStorage.getItem('userInfo')) : null


const shippingAddressFromStorage = localStorage.getItem('shippingAddress') ?
        JSON.parse(localStorage.getItem('shippingAddress')) : {}
        
const initialState={cart:  {cartItems: cartItemsfromlocalStorage,
                             shippingAddress: shippingAddressFromStorage},
                    userLogin:  {userInfo: userInfoFromStorage}
                    }

const middleware=[thunk] 

const store=createStore(reducer,initialState, 
    composeWithDevTools(applyMiddleware(...middleware)))//(applyMiddleware(thunk)) thunk-asynchronous

export default store