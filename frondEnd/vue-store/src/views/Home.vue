<template>
  <div class="home" id="home" name="home">
    <div class="block">
      <el-carousel height="460px">
        <el-carousel-item >
          <img style="height:460px;" src="../../public/imgs/anhbia.jpg"  />
        </el-carousel-item>
        <el-carousel-item >
          <img style="height:460px;" src="../../public/imgs/anhbia3.webp"  />
        </el-carousel-item>
        <el-carousel-item >
          <img style="height:460px;" src="../../public/imgs/anhbia4.jpg"  />
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="main-box">
      <div class="main">
        <div class="phone">
          <div class="box-hd">
            <div class="title">Books</div>
          </div>
          <div class="box-bd">
            <div class="promo-list">
              <router-link to>
                <img src="../../public/imgs/anh1.jpg" />
              </router-link>
            </div>
            <div class="list">
              <MyList :list="phoneList" :isMore="true"></MyList>
            </div>
          </div>
        </div>
        <div class="appliance" id="promo-menu">

          <div class="box-bd">
            <div class="promo-list">
              <ul>
                <li>
                  <img src="../../public/imgs/anh2.jpg" />
                </li>
                <li>
                  <img src="../../public/imgs/anh3.jpg" />
                </li>
              </ul>
            </div>
            <div class="list">
              <MyList :list="applianceList" :isMore="true"></MyList>
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
      phoneList: "",
      miTvList: "", 
      applianceList: "",
      applianceHotList: "", 
      accessoryList: "", 
      accessoryHotList: "", 
      protectingShellList: "", 
      chargerList: "", 
      applianceActive: 1, 
      accessoryActive: 1 
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
        this.getPromo("", "phoneList","/api/product/getPromoProduct");
        
      }else{
        this.getRecommend("", "phoneList")
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
    getPromo(categoryName, val, api) {
      api = api != undefined ? api : "/api/product/getPromoProduct";
      this.$axios
        .post(api, {

        })
        .then(res => {
          this[val] = res.data.Product;
        })
        .catch(err => {
          return Promise.reject(err);
        });
    },
    getRecommend(categoryName, val) {
      let api = "/api/user/recommend";
      this.$axios
        .post(api, {
          user_id :this.$store.getters.getUser.user_id
        })
        .then(res => {
          this[val] = res.data.Product;
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