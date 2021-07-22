import {
    CART_ADD_ITEM,
    CART_REMOVE_ITEM,
    CART_SAVE_SHIPPING_ADDRESS,

    CART_SAVE_PAYMENT_METHOD,

    CART_CLEAR_ITEMS,
} from '../constants/cartConstants'



export const cartReducer = (state = { cartItems: [], shippingAddress: {} }, action) => {
    switch (action.type) {
                case CART_ADD_ITEM:
                    const item = action.payload
                    const existItem = state.cartItems.find(x => x.product === item.product)// product is alias for id as sent by action

                    if (existItem) { //if the cart exists
                        return {
                            ...state,
                            cartItems: state.cartItems.map(x =>
                                x.product === existItem.product ? item : x)//if its not the product we ar looking for, return the same else return the updated value
                                
                        }

                    } else {
                        return {
                            ...state,//our original state(our state has several items and we send our rest of the items as it is just modify cartitems)
                            cartItems: [...state.cartItems, item]//add a new cartitem(just modify cart items)
                        }}
                    
                case CART_REMOVE_ITEM:
                    return {
                        ...state,
                        cartItems: state.cartItems.filter(x => x.product !== action.payload) //filter removes the id as soon as the equation becomes true
                    }
        
                case CART_SAVE_SHIPPING_ADDRESS:
                    return {
                        ...state,
                        shippingAddress: action.payload//form data
                    }
        
                case CART_SAVE_PAYMENT_METHOD:
                    return {
                        ...state,
                        paymentMethod: action.payload
                    }
        
                case CART_CLEAR_ITEMS:
                    return {
                        ...state,
                        cartItems: []
                    }   
            default:
                    return state
            
            
        }}

