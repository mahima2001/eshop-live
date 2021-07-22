import { Container } from 'react-bootstrap'
import { HashRouter as Router,Route  } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import Homescreen from './screens/Homescreen'
import ProductScreen from './screens/ProductScreen'
import CartScreen from './screens/cartScreen'
import LoginScreen from './screens/LoginScreen'
import ProfileScreen from './screens/ProfileScreen'
import RegisterScreen from './screens/RegisterScreen'
import ShippingScreen from './screens/ShippingScreen'
import PaymentScreen from './screens/PaymentScreen'
import PlaceOrderScreen from './screens/PlaceOrderScreen'
import OrderScreen from './screens/OrderScreen'
function App() {
  return (
    <Router>
      <Header/> 
      <main className="py-3">
        <Container>
        <Route exact path="/" component={Homescreen} />
        <Route path="/product/:id" component={ProductScreen} />
        <Route path="/cart/:id?" component={CartScreen} />
        {/* id is optionional if written after ? */}
        <Route path="/placeorder" component={PlaceOrderScreen} />
        <Route path='/order/:id' component={OrderScreen} />
        <Route path="/payment" component={PaymentScreen} />
        <Route path="/shipping" component={ShippingScreen} />
        <Route path="/profile" component={ProfileScreen} />
        <Route path="/register" component={RegisterScreen} />
        <Route path="/login" component={LoginScreen} />
        </Container>
      </main>
      <Footer/>
    </Router>
  );
}

export default App;
