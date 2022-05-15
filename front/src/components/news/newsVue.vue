<template>
  <div class="mb-16">
    <div>
      <h3 class="d-flex justify-center mb-10 mt-16">Новости</h3>
      <div class="d-flex justify-center flex-wrap">
        <div
            v-for="(item, index) in info"
            :key="index"
            class="d-flex"
        >
          <v-card
            max-width="400px"
            class="mx-7 mb-10"
          >
            <v-img
              :src="item.photo"
              height="300px"
            ></v-img>

            <v-card-title style="word-break: normal;">
              {{item.title}}
            </v-card-title>

            <!-- <v-card-subtitle>
              {{item.time_create}}
            </v-card-subtitle> -->

            <v-card-text>{{item.content}}</v-card-text>

          </v-card>
        </div>
      </div>
    </div>

    <h4 class="mb-5">Борьба с коррупцией</h4>
    <h6>Безусловные приоритеты АО «Каустик» — защита интересов потребителей, акционеров, партнеров и сотрудников Компании от угроз, связанных с коррупцией; повышение прозрачности бизнеса. </h6>
    <p>В случае, если Вам стало известно:</p>
    <ul>
      <li>о готовящихся или свершившихся фактах коррупции, мошенничества и хищений;</li>
      <li>о нарушениях при проведении закупочных процедур;</li>
      <li>о злоупотреблениях служебным положением и превышении полномочий должностными лицами;</li>
      <li>о совершении иных действий, которые наносят или могут нанести материальный ущерб или причинить вред деловой репутации АО «Каустик».</li>
    </ul>
    <template>
      <h5 class="mt-16">Просим немедленно сообщать об этом на «Горячую линию» по следующим адресам электронной почты:</h5>
      <v-simple-table class="my-10" dense>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                Направленность сообщений
              </th>
              <th class="text-left">
                Электронный адрес
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Приемная АО «Каустик»</td>
              <td><a href="mailto:	info@caustic.kz">	info@caustic.kz</a></td>
            </tr>
            <tr>
              <td>Служба безопасности </td>
              <td><a href="mailto:		sb@caustic.kz">		sb@caustic.kz</a></td>
            </tr>
            <tr>
              <td>Управление риск-менеджмента </td>
              <td><a href="mailto:urm@caustic.kz">urm@caustic.kz</a></td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </template>
    <p>Ваши обращения оперативно поступят в вышеуказанные департаменты, подчиняющиеся Совету директоров и не зависящие от руководства Компании.</p>
    <p>Все сообщения можно направлять как за личной подписью, так и анонимно. Руководство АО «Каустик» гарантирует, что не будет принимать никаких мер по установлению личности отправителя. Информация, полученная от вас, будет детально изучена и проверена.</p>
  </div>
</template>

<script>
import axios from "axios";
  export default {
    data: () => ({
      info: null,
    }),

    methods: {
    },
    mounted() {
      axios
        .get('http://127.0.0.1:8000/api/v1/artickeslist/')
        .then(response => (this.info = response.data))
        .catch(error => console.log(error));
      }
  }
</script>