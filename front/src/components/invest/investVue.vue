<template>
  <div>
    <v-card class="mb-10">
      <v-tabs vertical>
        <v-tab>
          <v-icon left color="primary">
            mdi-finance
          </v-icon>
          Финансовая отчетность
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-information-outline
          </v-icon>
          <div class="caption">Сведения о регистраторе и аудиторе</div>
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-calendar-text-outline
          </v-icon>
          Корпоративные события
        </v-tab>
        <v-tab-item>
          <v-card flat min-height="400px">
            <v-card-text>
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        ID
                      </th>
                      <th class="text-left">
                        Наименование
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(item, index) in finOtch"
                      :key="index"
                    >
                      <td>{{ index + 1 }}</td>
                      <td>{{item.title}}</td>
                      <td><a :href="item.file" download><v-icon color="primary">mdi-download-circle</v-icon></a></td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>  
            </v-card-text>
          </v-card>
        </v-tab-item> 
        <v-tab-item>
          <v-card flat min-height="400px">
            <v-card-text>
              <h6>ТОО «Делойт»</h6>
              <p>050059, Республика Казахстан
              г. Алматы, пр-т Аль-Фараби, 36</p>

              <p>Телефон: +7 727 258 13 40</p>
              <p>Факс: +7 727 258 13 41</p>
              <p>Email: almaty@deloitte.kz</p>

              <p>Лицензия на осуществление аудиторской деятельности № 0000015, серия МФЮ-2 от 13.09.2006 г. Лицензия выдана Министерством финансов Республики Казахстан. Срок действия: бессрочная.</p>

              <p>Полис обязательного страхования гражданско-правовой ответственности аудиторских организаций № ГО1719442 от 16.07.2014 г. Полис заключен с АО «Страховая Компания „Евразия“». Срок действия: 23.07.2014–22.07.2015 гг.</p>

              <p>ТОО «Делойт» является членом Палаты аудиторов Республики Казахстан.</p>
            </v-card-text>
          </v-card>
        </v-tab-item> 
        <v-tab-item>
          <v-card flat min-height="400px">
            <v-card-text>
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        ID
                      </th>
                      <th class="text-left">
                        Наименование
                      </th>
                      <th class="text-left">
                        Скачать
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(item, index)  in corpDoc"
                      :key="index"
                    >
                      <td>{{ index + 1 }}</td>
                      <td>{{item.title}}</td>
                      <td><a :href="item.file" download><v-icon color="primary">mdi-download-circle</v-icon></a></td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>   
            </v-card-text>
          </v-card>
        </v-tab-item> 
      </v-tabs>    
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
  export default {
    data: () => ({
      finOtch: [],
      corpDoc: [],
    }),
    mounted() {
      axios
        .get('http://127.0.0.1:8000/api/v1/documents/')
        .then(response => (response.data.forEach(element => {
            if (element.type_of_file === "Финансовая отчетность") {
              this.finOtch.push(element)
            }else if (element.type_of_file === "Корпоративные события") {
              console.log(element);
              this.corpDoc.push(element)
            }
          })))
        .catch(error => console.log(error));
    }
  }
</script>