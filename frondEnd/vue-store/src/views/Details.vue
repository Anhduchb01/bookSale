<template>
  <div id="details">
    <div class="page-header">
      <div class="title">
        <p>{{productDetails.product_name}}</p>
      </div>
    </div>
    <div class="main">
      <div class="block">
        <div >
          <img
            style="height:560px;"
            :src="productDetails.product_picture"    
          />
        </div>
      </div>
      <div class="content">
        <h1 class="name">{{productDetails.product_name}}</h1>
        <p class="intro">{{productDetails.product_intro}}</p>

        <div class="pro-list">
          <span class="pro-name">{{productDetails.product_name}}</span>
          <span class="pro-price">
            <span>{{productDetails.product_price}}$</span>
          </span>
          <p class="price-sum">Total : {{productDetails.product_price}}$</p>
        </div>
        <div class="button">
          <el-button class="shop-cart" :disabled="dis" @click="addShoppingCart">Add To Shopping Cart</el-button>
          <star-rating v-model="rating"  @rating-selected ="voteStar"></star-rating>       
        </div>

        <div class="pro-policy" >
          <ul>
            <li>
              <i class="el-icon-circle-check"></i> Xiaomi self-operated
            </li>
            <li>
              <i class="el-icon-circle-check"></i> millet delivery
            </li>
            <li>
              <i class="el-icon-circle-check"></i> 7 days no reason to return
            </li>
            <li>
              <i class="el-icon-circle-check"></i> 7 days price protection
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions } from "vuex";
import StarRating from 'vue-star-rating'
export default {
  components: {
    StarRating
  },
  data() {
    return {
      dis: false, 
      productID: "", 
      productDetails: "", 
      productPicture: "", 
      rating: 5
    };
  },
  activated() {
    if (this.$route.query.productID != undefined) {
      this.productID = this.$route.query.productID;
    }
  },
  watch: {
    productID: function(val) {
      this.getDetails(val);
    }
  },
  methods: {
    ...mapActions(["unshiftShoppingCart", "addShoppingCartNum"]),
    getDetails(val) {
      this.$axios
        .get("/api/product/getDetails?productID="+val)
        .then(res => {
          this.productDetails = res.data.Product;
        })
        .catch(err => {
          return Promise.reject(err);
        });
    },
    addShoppingCart() {
      if (!this.$store.getters.getUser) {
        this.$store.dispatch("setShowLogin", true);
        return;
      }
      this.$axios
        .post("/api/user/shoppingCart/addShoppingCart", {
          user_id: this.$store.getters.getUser.user_id,
          product_id: this.productID
        })
        .then(res => {
          switch (res.data.code) {
            case "001":
              this.unshiftShoppingCart(res.data.shoppingCartData[0]);
              this.notifySucceed(res.data.msg);
              break;
            case "002":
              this.addShoppingCartNum(this.productID);
              this.notifySucceed(res.data.msg);
              break;
            case "003":
              this.dis = true;
              this.notifyError(res.data.msg);
              break;
            default:
              this.notifyError(res.data.msg);
          }
        })
        .catch(err => {
          return Promise.reject(err);
        });
    },
    voteStar() {
      if (!this.$store.getters.getUser) {
        this.$store.dispatch("setShowLogin", true);
        return;
      }
      this.$axios
        .post("/api/user/voteStar", {
          user_id: this.$store.getters.getUser.user_id,
          product_id: this.productID,
          star :this.rating
        })
        .then(res => {
          switch (res.data.code) {
            case "001":
              this.notifySucceed(res.data.msg);
              break;
            case "002":
              this.notifyError(res.data.msg);
              break;
            default:
              this.notifySucceed(res.data.msg);
          }
        })
        .catch(err => {
          return Promise.reject(err);
        });
    },
  }
};
</script>
<style>
/* 头部CSS */
#details .page-header {
  height: 64px;
  margin-top: -20px;
  z-index: 4;
  background: #fff;
  border-bottom: 1px solid #e0e0e0;
  -webkit-box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.07);
  box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.07);
}
#details .page-header .title {
  width: 1225px;
  height: 64px;
  line-height: 64px;
  font-size: 18px;
  font-weight: 400;
  color: #212121;
  margin: 0 auto;
}
#details .page-header .title p {
  float: left;
}
#details .page-header .title .list {
  height: 64px;
  float: right;
}
#details .page-header .title .list li {
  float: left;
  margin-left: 20px;
}
#details .page-header .title .list li a {
  font-size: 14px;
  color: #616161;
}
#details .page-header .title .list li a:hover {
  font-size: 14px;
  color: #ff6700;
}
#details .main {
  width: 1225px;
  height: 560px;
  padding-top: 30px;
  margin: 0 auto;
}
#details .main .block {
  float: left;
  width: 560px;
  height: 560px;
}
#details .el-carousel .el-carousel__indicator .el-carousel__button {
  background-color: rgba(163, 163, 163, 0.8);
}
#details .main .content {
  float: left;
  margin-left: 25px;
  width: 640px;
}
#details .main .content .name {
  height: 30px;
  line-height: 30px;
  font-size: 24px;
  font-weight: normal;
  color: #212121;
}
#details .main .content .intro {
  color: #b0b0b0;
  padding-top: 10px;
}
#details .main .content .store {
  color: #ff6700;
  padding-top: 10px;
}
#details .main .content .price {
  display: block;
  font-size: 18px;
  color: #ff6700;
  border-bottom: 1px solid #e0e0e0;
  padding: 25px 0 25px;
}
#details .main .content .price .del {
  font-size: 14px;
  margin-left: 10px;
  color: #b0b0b0;
  text-decoration: line-through;
}
#details .main .content .pro-list {
  background: #f9f9fa;
  padding: 30px 60px;
  margin: 50px 0 50px;
}
#details .main .content .pro-list span {
  line-height: 30px;
  color: #616161;
}
#details .main .content .pro-list .pro-price {
  float: right;
}
#details .main .content .pro-list .pro-price .pro-del {
  margin-left: 10px;
  text-decoration: line-through;
}
#details .main .content .pro-list .price-sum {
  color: #ff6700;
  font-size: 24px;
  padding-top: 20px;
}
#details .main .content .button {
  height: 55px;
  margin: 10px 0 20px 0;
}
#details .main .content .button .el-button {
  float: left;
  height: 55px;
  font-size: 16px;
  color: #fff;
  border: none;
  text-align: center;
}
.shop-cart{
  width: 270px !important;
  margin-right: 50px;
}
#details .main .content .button .shop-cart {
  width: 340px;
  background-color: #ff6700;
}
#details .main .content .button .shop-cart:hover {
  background-color: #f25807;
}

#details .main .content .button .like {
  width: 260px;
  margin-left: 40px;
  background-color: #b0b0b0;
}
#details .main .content .button .like:hover {
  background-color: #757575;
}
#details .main .content .pro-policy li {
  float: left;
  margin-right: 20px;
  color: #b0b0b0;
}
.pro-policy{
  padding-top: 20px;
}
/* 主要内容CSS END */
</style>