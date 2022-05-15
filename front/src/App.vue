<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dense
      dark
    >
      <v-toolbar-title>
        <router-link tag="button" to="/">Акционерное общество «Каустик»</router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <router-link tag="button" to="/about" class="ml-6">О компании</router-link>
      <router-link tag="button" to="/invest" class="ml-6">Акционерам и инфесторам</router-link>
      <router-link tag="button" to="/projects" class="ml-6">Проекты</router-link>
      <router-link tag="button" to="/ecology" class="ml-6">Экология</router-link>
      <router-link tag="button" to="/career" class="ml-6">Карьера</router-link>
      <router-link tag="button" to="/service" class="ml-6">Услуги</router-link>
      <router-link tag="button" to="/news" class="ml-6">Пресс-центр</router-link>
    </v-app-bar>
    
    <v-main class="container">
      <router-view></router-view>
    </v-main>

    <v-footer
      dark
      padless
    >
      <v-card
        flat
        tile
        width="100%"
        class="px-16"
      >
        <v-row>
          <v-col
            cols="12"
            sm="3"
            class="d-flex flex-column py-7"
          >
            <p>140000, Республика Казахстан г. Павлодар, промышленная зона северная, строение 28/1</p> 
            <div class="d-flex align-center">
              <v-icon class="mr-3">mdi-email-edit</v-icon>
              <a href="mailto:info@caustic.kz"> info@caustic.kz</a>
            </div>
          </v-col>
          <v-col
            cols="12"
            sm="3"
            class="d-flex flex-column py-7"
          >
            <p>Приемная</p>
            <div class="d-flex align-center">
              <v-icon class="mr-3">mdi-phone</v-icon>
              <a href="tel:+77182731201">+7 (7182) 73-12-01</a>
            </div>
          </v-col>
          <v-col
            cols="12"
            sm="3"
            class="d-flex flex-column py-7"
          >
            <p>Отдел реализации</p>
            <div class="d-flex align-center">
              <v-icon class="mr-3">mdi-phone</v-icon>
              <a href="tel:+7(7182)73-12-08">+7 (7182) 73-12-08</a>
            </div>
            <p>(доб. 230, 233)</p>
          </v-col>
          <v-col
            cols="12"
            sm="3"
            class="d-flex flex-column py-7"
          >
            <p>Отдел закупок</p>
            <div class="d-flex align-center">
              <v-icon class="mr-3">mdi-phone</v-icon>
              <a href="tel:+7(7182)73-12-25">+7 (7182) 73-12-25</a>
            </div>
            <p>(470 Ангелина)<br>
            (270 Вера)<br>
            (237 Адиль)</p>
          </v-col>
        </v-row>

        <v-divider></v-divider>

        <v-card-text class="white--text d-flex justify-center">
          {{ new Date().getFullYear() }} — <strong> АО «КАУСТИК»</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>
<script>
import axios from "axios";

export default {
  name: 'App',
  mounted(){
    axios.post('http://127.0.0.1:8000/api/v1/user/', {
    username: 'user34',
    password: 'password123'
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });

  }
}
</script>

<style>
  a{
    text-decoration: none;
  }
  .container{
    max-width: 1400px;
  }
</style>