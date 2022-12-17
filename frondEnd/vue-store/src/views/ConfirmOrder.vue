
<template>
  <div class="confirmOrder">

    <div class="confirmOrder-header">
      <div class="header-content">
        <p>
          <i class="el-icon-s-order"></i>
        </p>
        <p>Confirm Order</p>
        <router-link to></router-link>
      </div>
    </div>
    <div class="content">
      <div class="section-address">
        <p class="title">Shipping address</p>
        <div class="address-body">
          <ul>
            <li
              :class="item.id == confirmAddress ? 'in-section' : ''"
              v-for="item in address"
              :key="item.id"
            >
              <h2>{{item.name}}</h2>
              <p class="phone">{{item.phone}}</p>
              <p class="address">{{item.address}}</p>
            </li>
            <li class="add-address">
              <i class="el-icon-circle-plus-outline"></i>
              <p>Add New Address</p>
            </li>
          </ul>
        </div>
      </div>
      <div class="section-goods">
        <p class="title">Products and Coupons</p>
        <div class="goods-list">
          <ul>
            <li v-for="item in getCheckGoods" :key="item.id">
              <img :src="item.productImg" />
              <span class="pro-name">{{item.productName}}</span>
              <span class="pro-price">{{item.price}}$ x {{item.num}}</span>
              <span class="pro-status"></span>
              <span class="pro-total">{{item.price * item.num}}$</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="section-shipment">
        <p class="title">Delivery Method</p>
        <p class="shipment">Free Shipping</p>
      </div>
      <div class="section-invoice">
        <p class="title">Invoice</p>
        <p class="invoice">E-Invoice</p>
        <p class="invoice">Personal</p>
        <p class="invoice">Commodity Details</p>
      </div>
      <div class="section-count">
        <div class="money-box">
          <ul>
            <li>
              <span class="title">Number : </span>
              <span class="value">{{getCheckNum}}</span>
            </li>
            <li>
              <span class="title">Total Price: </span>
              <span class="value">{{getTotalPrice}}$</span>
            </li>
            <li>
              <span class="title">Event Offers: </span>
              <span class="value">-0$</span>
            </li>
            <li>
              <span class="title">Coupon deduction: </span>
              <span class="value">-0$</span>
            </li>
            <li>
              <span class="title">Freight: </span>
              <span class="value">0$</span>
            </li>
            <li class="total">
              <span class="title">Total: </span>
              <span class="value">
                <span class="total-price">{{getTotalPrice}}</span>$
              </span>
            </li>
          </ul>
        </div>
      </div>
      <div class="section-bar">
        <div class="btn">
          <router-link to="/shoppingCart" class="btn-base btn-return">Return To Shopping Cart</router-link>
          <a href="javascript:void(0);" @click="addOrder" class="btn-base btn-primary">Settlement</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
export default {
  name: "",
  data() {
    return {
      confirmAddress: 1, 
      address: [
        {
          id: 1,
          name: "User1",
          phone: "0123456789",
          address: "Viet Nam"
        },
        {
          id: 2,
          name: "User2",
          phone: "0987654321",
          address: "Japan"
        }
      ]
    };
  },
  created() {
    if (this.getCheckNum < 1) {
      this.notifyError("Please check the items before checkout");
      this.$router.push({ path: "/shoppingCart" });
    }
  },
  computed: {
    ...mapGetters(["getCheckNum", "getTotalPrice", "getCheckGoods"])
  },
  methods: {
    ...mapActions(["deleteShoppingCart"]),
    addOrder() {   
      this.$axios
        .post("/api/user/order/addOrder", {
          user_id: this.$store.getters.getUser.user_id,
          products: this.getCheckGoods
        })
        .then(res => {
          let products = this.getCheckGoods;
          switch (res.data.code) {
            case "001":
              for (let i = 0; i < products.length; i++) {
                const temp = products[i];
                this.deleteShoppingCart(temp.id);
              }
              this.notifySucceed(res.data.msg);
              this.$router.push({ name: 'Home' })
              break;
            default:
              this.notifyError(res.data.msg);
          }
        })
        .catch(err => {
          return Promise.reject(err);
        });
    
    }
  }
};
</script>
<style scoped>
.confirmOrder {
  background-color: #f5f5f5;
  padding-bottom: 20px;
}
.confirmOrder .confirmOrder-header {
  background-color: #fff;
  border-bottom: 2px solid #ff6700;
  margin-bottom: 20px;
}
.confirmOrder .confirmOrder-header .header-content {
  width: 1225px;
  margin: 0 auto;
  height: 80px;
}
.confirmOrder .confirmOrder-header .header-content p {
  float: left;
  font-size: 28px;
  line-height: 80px;
  color: #424242;
  margin-right: 20px;
}
.confirmOrder .confirmOrder-header .header-content p i {
  font-size: 45px;
  color: #ff6700;
  line-height: 80px;
}
.confirmOrder .content {
  width: 1225px;
  margin: 0 auto;
  padding: 48px 0 0;
  background-color: #fff;
}

.confirmOrder .content .section-address {
  margin: 0 48px;
  overflow: hidden;
}
.confirmOrder .content .section-address .title {
  color: #333;
  font-size: 18px;
  line-height: 20px;
  margin-bottom: 20px;
}
.confirmOrder .content .address-body li {
  float: left;
  color: #333;
  width: 220px;
  height: 178px;
  border: 1px solid #e0e0e0;
  padding: 15px 24px 0;
  margin-right: 17px;
  margin-bottom: 24px;
}
.confirmOrder .content .address-body .in-section {
  border: 1px solid #ff6700;
}
.confirmOrder .content .address-body li h2 {
  font-size: 18px;
  font-weight: normal;
  line-height: 30px;
  margin-bottom: 10px;
}
.confirmOrder .content .address-body li p {
  font-size: 14px;
  color: #757575;
}
.confirmOrder .content .address-body li .address {
  padding: 10px 0;
  max-width: 180px;
  max-height: 88px;
  line-height: 22px;
  overflow: hidden;
}
.confirmOrder .content .address-body .add-address {
  text-align: center;
  line-height: 30px;
}
.confirmOrder .content .address-body .add-address i {
  font-size: 30px;
  padding-top: 50px;
  text-align: center;
}
.confirmOrder .content .section-goods {
  margin: 0 48px;
}
.confirmOrder .content .section-goods p.title {
  color: #333;
  font-size: 18px;
  line-height: 40px;
}
.confirmOrder .content .section-goods .goods-list {
  padding: 5px 0;
  border-top: 1px solid #e0e0e0;
  border-bottom: 1px solid #e0e0e0;
}
.confirmOrder .content .section-goods .goods-list li {
  padding: 10px 0;
  color: #424242;
  overflow: hidden;
}
.confirmOrder .content .section-goods .goods-list li img {
  float: left;
  width: 30px;
  height: 30px;
  margin-right: 10px;
}
.confirmOrder .content .section-goods .goods-list li .pro-name {
  float: left;
  width: 650px;
  line-height: 30px;
}
.confirmOrder .content .section-goods .goods-list li .pro-price {
  float: left;
  width: 150px;
  text-align: center;
  line-height: 30px;
}
.confirmOrder .content .section-goods .goods-list li .pro-status {
  float: left;
  width: 99px;
  height: 30px;
  text-align: center;
  line-height: 30px;
}
.confirmOrder .content .section-goods .goods-list li .pro-total {
  float: left;
  width: 190px;
  text-align: center;
  color: #ff6700;
  line-height: 30px;
}
.confirmOrder .content .section-shipment {
  margin: 0 48px;
  padding: 25px 0;
  border-bottom: 1px solid #e0e0e0;
  overflow: hidden;
}
.confirmOrder .content .section-shipment .title {
  float: left;
  width: 150px;
  color: #333;
  font-size: 18px;
  line-height: 38px;
}
.confirmOrder .content .section-shipment .shipment {
  float: left;
  line-height: 38px;
  font-size: 14px;
  color: #ff6700;
}
.confirmOrder .content .section-invoice {
  margin: 0 48px;
  padding: 25px 0;
  border-bottom: 1px solid #e0e0e0;
  overflow: hidden;
}
.confirmOrder .content .section-invoice .title {
  float: left;
  width: 150px;
  color: #333;
  font-size: 18px;
  line-height: 38px;
}
.confirmOrder .content .section-invoice .invoice {
  float: left;
  line-height: 38px;
  font-size: 14px;
  margin-right: 20px;
  color: #ff6700;
}
.confirmOrder .content .section-count {
  margin: 0 48px;
  padding: 20px 0;
  overflow: hidden;
}
.confirmOrder .content .section-count .money-box {
  float: right;
  text-align: right;
}
.confirmOrder .content .section-count .money-box .title {
  float: left;
  width: 126px;
  height: 30px;
  display: block;
  line-height: 30px;
  color: #757575;
}
.confirmOrder .content .section-count .money-box .value {
  float: left;
  min-width: 105px;
  height: 30px;
  display: block;
  line-height: 30px;
  color: #ff6700;
}
.confirmOrder .content .section-count .money-box .total .title {
  padding-top: 15px;
}
.confirmOrder .content .section-count .money-box .total .value {
  padding-top: 10px;
}
.confirmOrder .content .section-count .money-box .total-price {
  font-size: 30px;
}
.confirmOrder .content .section-bar {
  padding: 20px 48px;
  border-top: 2px solid #f5f5f5;
  overflow: hidden;
}
.confirmOrder .content .section-bar .btn {
  float: right;
}
.confirmOrder .content .section-bar .btn .btn-base {
  float: left;
  margin-left: 30px;
  width: 158px;
  height: 38px;
  border: 1px solid #b0b0b0;
  font-size: 14px;
  line-height: 38px;
  text-align: center;
}
.confirmOrder .content .section-bar .btn .btn-return {
  color: rgba(0, 0, 0, 0.27);
  border-color: rgba(0, 0, 0, 0.27);
}
.confirmOrder .content .section-bar .btn .btn-primary {
  background: #ff6700;
  border-color: #ff6700;
  color: #fff;
}
</style>