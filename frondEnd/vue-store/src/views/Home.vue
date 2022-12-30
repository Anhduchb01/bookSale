<template>
  <div class="home" id="home" name="home">
    <div class="block">
      <el-carousel height="460px">
        <el-carousel-item >
          <img class="item__image" style="height:100%;width :100%" src="../../public/imgs/bia1.jpg"  />
        </el-carousel-item>
        <el-carousel-item >
          <img class="item__image"  style="height:100%;width :100%" src="../../public/imgs/bia2.jpg"  />
        </el-carousel-item>
        <el-carousel-item >
          <img class="item__image" style="height:100%;width :100%" src="../../public/imgs/bia3.jpg"  />
        </el-carousel-item>
        <el-carousel-item >
          <img class="item__image" style="height:100%;width :100%" src="../../public/imgs/bia4.jpg"  />
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="main-box">
      <div class="main">
        <div class="phone">
          <div class="box-hd">
            <h1 class="title">Books</h1>
          </div>
          <div class="box-bd">
            <div class="promo-list">
              <h3 v-if="showText">Collaborative filtering by product rating</h3>
            </div>
            <div class="list">
              <MyList :list="listProductCf" :isMore="true"></MyList>
            </div>
          </div>
          <div class="box-bd">
            <div class="promo-list">
              <h3 v-if="showText"> Collaborative filtering by author rating</h3>
            </div>
            <div class="list">
              <MyList :list="listProductAuthor" :isMore="true"></MyList>
            </div>
          </div>
          <div class="box-bd">
            <div class="promo-list">
              <h3 v-if="showText">Content based by product rating</h3>
            </div>
            <div class="list">
              <MyList :list="listProductCb" :isMore="true"></MyList>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import { mapGetters } from "vuex";
export default {
  data() {
    return {
      carousel: "", 
      listProductCb :"",
      listProductCf :"",
      listProductAuthor :"",
      miTvList: "", 
      applianceList: "",
      applianceHotList: "", 
      accessoryList: "", 
      accessoryHotList: "", 
      protectingShellList: "", 
      chargerList: "", 
      applianceActive: 1, 
      accessoryActive: 1 ,
      showText : false
    };
  },
  watch: {
 
    applianceActive: function(val) {
      if (this.applianceHotList == "") {
        this.applianceHotList = this.applianceList;
      }
      if (val == 1) {
        this.applianceList = this.applianceHotList;
        return;
      }
      if (val == 2) {
        this.applianceList = this.miTvList;
        return;
      }
    },
    accessoryActive: function(val) {
      if (this.accessoryHotList == "") {
        this.accessoryHotList = this.accessoryList;
      }
      if (val == 1) {
        this.accessoryList = this.accessoryHotList;
        return;
      }
      if (val == 2) {
        this.accessoryList = this.protectingShellList;
        return;
      }
      if (val == 3) {
        this.accessoryList = this.chargerList;
        return;
      }
    }
  },
  created() {
    if (!this.$store.getters.getUser) {
        this.getPromo("", "listProductCb","listProductCf","listProductAuthor","/api/product/getPromoProduct");
        
      }else{
          this.getRecommend("", "listProductCb","listProductCf","listProductAuthor")
      }
  },
  computed: {
    ...mapGetters(["getUser"])
  },
  methods: {
    getChildMsg(val) {
      this.applianceActive = val;
    },
    getChildMsg2(val) {
      this.accessoryActive = val;
    },
    getPromo(categoryName, val,val2,val3, api) {
      this.showText =false
      api = api != undefined ? api : "/api/product/getPromoProduct";
      this.$axios
        .post(api, {

        })
        .then(res => {
          this[val] = res.data.ProductRatingCb;
          this[val2]=res.data.ProductRatingCf;
          this[val3]=res.data.ProductRatingAuthor;

        })
        .catch(err => {
          return Promise.reject(err);
        });
    },
    getRecommend(categoryName, val,val2,val3) {

      let api = "/api/user/recommend";
      this.$axios
        .post(api, {
          user_id :this.$store.getters.getUser.user_id
        })
        .then(res => {
          this.showText =true
          this[val] = res.data.ProductRatingCb;
          this[val2]=res.data.ProductRatingCf;
          this[val3]=res.data.ProductRatingAuthor;

          this[val] = this[val].filter((value, index, self) =>
            index === self.findIndex((t) => (
              t.product_id === value.product_id
            ))
          )
        })
        .catch(err => {
          return Promise.reject(err);
        });
    },
  }
};
</script>
<style scoped>
@import "../assets/css/index.css";
</style>
<style>
#app{
    font-family: Inter,sans-serif;
}
</style>