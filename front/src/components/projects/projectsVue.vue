<template>
  <div class="scroll mb-10">
    <h3 class="my-10">Поставщикам и подрядчикам</h3>
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
            v-for="(item, index)  in projDocs"
            :key="index"
          >
            <td>{{ index + 1 }}</td>
            <td>{{item.title}}</td>
            <td><a :href="item.file" download><v-icon color="dark">mdi-download-circle</v-icon></a></td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>   
  </div>
</template>

<script>
import axios from "axios";
  export default {
    data: () => ({
      projDocs: [],
    }),
    mounted() {
      axios
        .get('http://127.0.0.1:8000/api/v1/documents/')
        .then(response => (response.data.forEach(element => {
            console.log(element)
            if (element.type_of_file === "Корпоративные события") {
              this.projDocs.push(element)
            }
          })))
        .catch(error => console.log(error));
    }
  }
</script>

<style>
.scroll{
  overflow: auto;
}
</style>