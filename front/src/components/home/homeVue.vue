<template>
  <div>
    <v-card class="mb-10">
      <v-tabs vertical>
        <v-tab>
          <v-icon left color="green">
            mdi-leaf-circle
          </v-icon>
          Экология
        </v-tab>
        <v-tab>
          <v-icon left color="purple">
            mdi-human-handsup
          </v-icon>
          Карьера
        </v-tab>

        <v-tab-item>
          <v-card flat class="backimage1" min-height="400px">
            <v-card-text>
              <div class="blurcard">
                <h3>Экология</h3>
                <p>
                  Технология мембранного электролиза полностью исключает воздействие на окружающую среду
                </p>
                <div class="d-flex justify-end">
                  <v-btn 
                    color="primary" 
                    outlined
                    @click="$router.push('/ecology')"
                  ><v-icon class="mr-3 ml-n2">mdi-dots-horizontal-circle-outline</v-icon> Подробнее</v-btn>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat class="backimage" min-height="400px">
            <v-card-text>
              <div class="blurcard">
                <h3>Карьера</h3>
                <p>
                  АО «Каустик» предоставляет широкий спектр возможностей карьерного роста внутри различных подразделений Компании
                </p>
                <div class="d-flex justify-end">
                  <v-btn 
                    color="primary" 
                    outlined
                    @click="$router.push('/career')"
                  ><v-icon class="mr-3 ml-n2">mdi-dots-horizontal-circle-outline</v-icon> Подробнее</v-btn>
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
    <v-row class="mb-10" style="border-bottom: 1px solid grey;">
      <v-col
        cols="12"
        sm="7"
        class="mt-5 px-16 d-flex flex-column"
      >
        <h5>О компании</h5>
        <p>Акционерное общество «Каустик» — это современное химическое производство, соответствующее высочайшим казахстанским и международным стандартам качества.</p>
        <p>Открытие завода АО «Каустик» состоялось в октябре 2011 года, инвестиции в его строительство составили более 108 млн долл. США. Проектная мощность — 30 тыс. тонн каустической соды, 6.6 тыс. тонн гипохлорита натрия, 26.4 тыс. тонн хлора и 45 тыс. тонн соляной кислоты в год.</p>
        <v-btn 
          class="align-self-end"
          color="primary"
          text
          @click="$router.push('/about')"
        >Подробнее</v-btn>
      </v-col>
      <v-col
        cols="12"
        sm="5"
        class="mt-5 px-16 d-flex flex-column align-end"
      >

        <v-card
          max-width="344"
          outlined
        >
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                <v-btn
                  text
                  color="primary"
                  @click.stop="dialog = true"
                >
                  Все вакансии
                </v-btn>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
    <div class="news">
      <h3 class="d-flex justify-center mb-10 mt-16">Последние новости</h3>
      <div class="d-flex justify-center">
        <div
            v-for="(item, index) in cardData"
            :key="index"
        >
          <v-card
            max-width="400"
            class="mx-7"
            style="position:static;"
          >
            <v-img
              :src="item.photo"
              height="200px"
            ></v-img>

            <v-card-title class="" style="word-break: normal;">
              {{item.title}}
            </v-card-title>

            <v-card-subtitle>
              {{item.date}}
            </v-card-subtitle>


            <v-card-text>{{item.content}}</v-card-text>

            <v-expand-transition>
              <div v-show="item.showDescribe">
                <v-divider></v-divider>

                <v-card-text>
                  {{item.content}}
                </v-card-text>
              </div>
            </v-expand-transition>
          </v-card>
        </div>
      </div>
    </div>
    <v-dialog
      v-model="dialog"
      max-width="500"
    >
      <v-card>
        <v-card-title class="text-h5">
          Вакансии
        </v-card-title>

        <v-card-text>
          <p>На этой странице публикуются открытые вакансии АО «Каустик». Если на текущий момент свободных вакансий нет, Вы можете отправить свое резюме в целях включения Вашей кандидатуры в банк вакансий Компании. В письме просим Вас указывать название текущей или потенциальной вакансии.</p>

          <p>Отдел кадров АО «Каустик»:</p>
          <p>Телефон:<a href="tel:+7 (7182) 39-08-17">+7 (7182) 39-08-17</a></p>
          <p>Факс:<a href="tel:++7 (7182) 33-36-88">+7 (7182) 33-36-88</a></p>
          <ul>
            <li v-for="(item, index) in infoVac" :key="index">{{item.title}} <p class="ml-5">{{item.description}}</p></li>
          </ul>
          
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Закрыть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </div>
</template>

<script>
import axios from "axios";
  export default {
    data: () => ({
      dialog: false,
      infoVac: null,
      cardData: [],
    }),

    methods: {
      getInfo () {
        axios
          .get('http://127.0.0.1:8000/api/v1/vacancii/')
          .then(response => (this.infoVac = response.data))
          .catch(error => console.log(error))
      }
    },
    mounted() {
      this.getInfo()

      axios
        .get('http://127.0.0.1:8000/api/v1/artickeslist/')
        .then(response => (response.data.forEach(element => {
            if (this.cardData.length !== 3) {
              this.cardData.push(element) 
            }
          })
        ))
        .catch(error => console.log(error))
    }

}
</script>

<style>
  .theme--light.v-tabs>.v-tabs-bar{
    border-right: 1px solid rgb(117, 117, 117);
    border-radius: 0px;
  }
  .backimage{
    background-image: url(../../assets/home-images/slide3.jpg);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  .backimage1{
    background-image: url(../../assets/home-images/slide2.jpg);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  .blurcard{
    background-color: rgba(236, 236, 236, 0.733);
    width: 50%;
    padding: 20px;
    border-radius: 10px 20px 40px 10px;
    box-shadow: 3px 3px rgb(64, 92, 172);
  }
  .news{ 
    height: 900px;
  }
</style>