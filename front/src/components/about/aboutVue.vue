<template>
  <div>
    <v-card class="mb-10">
      <v-tabs vertical>
        <v-tab>
          <v-icon left color="primary">
            mdi-information-variant
          </v-icon>
          О компании
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-pillar
          </v-icon>
          История
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-chart-ppf
          </v-icon>
          Продукция
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-account-hard-hat
          </v-icon>
          Стркутура
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-strategy
          </v-icon>
          Стратегия
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-text-box-multiple-outline
          </v-icon>
          Корпоративные документы
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-file-document
          </v-icon>
          Разрешительные документы
        </v-tab>
        <v-tab>
          <v-icon left color="primary">
            mdi-card-account-phone-outline
          </v-icon>
          Контакты
        </v-tab>

        <v-tab-item>
          <v-card flat min-height="400px">
            <v-card-text>
              <h6>Акционерное общество «Каустик» (АО «Каустик», Компания) — это современное химическое производство, соответствующее высочайшим казахстанским и международным стандартам качества</h6>
              <p>
                Открытие завода АО «Каустик» состоялось в октябре 2011 года, инвестиции в его строительство составили более 108 млн долл. США. Проектная мощность — 30 тыс. тонн каустической соды, 6,6 тыс. тонн гипохлорита натрия, 26,4 тыс. тонн хлора и 45 тыс. тонн соляной кислоты в год.
              </p>
              <p>
                До 2011 года основным источником поставок данной продукции на казахстанский рынок являлся импорт из России, Узбекистана и Китая. С выходом на рынок АО «Каустик» ситуация изменилась: выпускаемая заводом продукция поставляется как на казахстанский рынок (полностью замещая импорт), так и экспортируется в страны СНГ и дальнее зарубежье.
              </p>
              <p>
                Высокий уровень качества выпускаемой продукции отмечен основными потребителями продукции, в число которых входят компании АО «НАК Казатомпром», АО «Усть-Каменогорский титано-магниевый комбинат», АО «Алюминий Казахстана», АО «Павлодарский нефтехимический завод», АО «АрселорМиттал Темиртау», ТОО «Тенгизшевройл», Hulliburton, Schlumberge, организации водоснабжения и пр.
              </p>
              <p>
                АО «Каустик» развивает проект в рамках реализации поручения Президента Республики Казахстан Нурсултана Назарбаевапо формированию полноценного химического кластера на базе свободной экономической зоны «Павлодар».
              </p>
              <p>На площадке АО «Каустик» планируется организация ряда импортозамещающих производств, совместно с АО «НАК «Казатомпром». В частности, увеличение мощности производства каустической соды, хлора, соляной кислоты и запуск производства перекиси водорода, используемых при добыче и переработке урана, а также хлора для производства редких и редкоземельных металлов и реагентов.</p>
              <p>Кроме того, планируется создание производства реагентов для очистки и дезинфекции питьевой воды на основе трансферта передовых мировых технологий.</p>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card>
            <v-card-text>
              <v-timeline>
                <v-timeline-item
                  v-for="(year, i) in years"
                  :key="i"
                  :color="year.color"
                  small
                >
                  <template v-slot:opposite>
                    <span
                      :class="`headline font-weight-bold ${year.color}--text`"
                      v-text="year.year"
                    ></span>
                  </template>
                  <div class="py-4">
                    <div>
                      {{year.text}}
                    </div>
                  </div>
                </v-timeline-item>
              </v-timeline>
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card>
            <v-card-text>
              <h6>Продукция Сода каустическая</h6>
              <p>NaOH — ГОСТ 2263-79</p>
              <p>Объем производства 30 тыс. тонн в год.</p>

              <p>Продукт марки РХ в водном растворе с содержанием основного вещества 50%, твердая чешуированная с содержанием основного вещества 98,8%.</p>

              <p>Применяется практический во всех отраслях промышленности: в черной и цветной металлургии, легкой, пищевой, на предприятиях энергетики, где является незаменимым реагентом в системах водоподготовки.</p>

              <h6>Хлор жидкий</h6>
              
              <p>Cl2 — ГОСТ 6718-93</p>

              <p>Объем производства 26 тыс. тонн в год</p>

              <p>Объемная доля хлора не менее 99,8%.</p>

              <p>Дезинфицирующий реагент, применяющийся при подготовке воды и при обеззараживании сточных вод, также хлорирующий агент в химической промышленности и цветной металлургии.</p>

              <h6>Кислота соляная</h6>
              <p>HCl — ГОСТ 857-95</p>

              <p>Объем производства 45 тыс. тонн в год</p>

              <p>Водный раствор с содержанием основного вещества 35%.</p>

              <p>Применяется в нефтяной, химической, медицинской, пищевой промышленностях, цветной и черной металлургии.</p>

              <h6>Гипохлорит натрия технический</h6>
              <p>NaClO — ГОСТ 11086-76</p>

              <p>Объем производства 6,6 тыс. тонн в год</p>

              <p>Массовая концентрация активного хлора не менее 180 г/дм3.</p>

              <p>Применяется для обеззараживания бытовых и промышленных сточных вод, питьевой воды и воды плавательных бассейнов, санитарно-бытовых помещений, плавательных бассейнов, санитарно-бытовых помещений, для дезинфекции в быту, больницах и лечебно-оздоровительных учреждениях, оборудования, белья, хозяйственно и другого инвентаря, для отбеливания бумаги, ваты, хлопка, ткани, целлюлозы и т.д.</p>
            </v-card-text>
          </v-card>
        </v-tab-item> 
        <v-tab-item>
          <v-card>
            <v-card-text>
              <img src="../../assets/structure_ru.jpg" alt="">
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card>
            <v-card-text>
              <h6>Стратегия развития АО «Каустик» базируется на следующих принципах:</h6>
              <ul>
                <li>ориентированность на будущее;</li>
                <li>экономическая эффективность;</li>
                <li>социальная ответственность;</li>
                <li>охрана окружающей среды.</li>
              </ul>
              
              <h6>Задачи:</h6>
              <ul>
                <li>развитие базовой отрасли химической промышленности Республики Казахстан;</li>
                <li>создание новых, экспортоориентированных производств продукции с высокой добавленной стоимостью в рамках развития химической отрасли Республики Казахстан;</li>
                <li>создание новых рабочих мест в Павлодарской области.</li>
              </ul>
              
              <h6>Направления развития:</h6>
              <ul>
                <li>расширение имеющихся производственных мощностей (хлор-щелочное производство);</li>
                <li>создание совместных предприятий как с отечественными, так и с зарубежными партнерами;
                выход на новые продуктовые и региональные рынки;</li>
                <li>организация производств товаров народного потребления и пр.</li>
              </ul>

              <h6>Основные мероприятия:</h6>
              <ul>
                <li>расширение хлор-щелочного производства до 100 000 тонн/год;</li>
                <li>организация производства товаров народного потребления (бытовая химия) на базе хлор-щелочного производства;</li>
                <li>организация совместного предприятия с ТОО «Казфосфат» (Казахстан, г. Тараз), Lanxess (Германия) по производству треххлористого фосфора на базе хлор-щелочного производства АО «Каустик»;</li>
                <li>проработка стратегии организации производств продукции с высокой добавленной стоимостью на базе расширения хлор-щелочного производства АО «Каустик».</li>
              </ul>              
            </v-card-text>
          </v-card>
        </v-tab-item>
         <v-tab-item>
          <v-card>
            <v-card-text>
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        Наименование
                      </th>
                      <th class="text-left">
                        
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="item in corpDoc"
                      :key="item.name"
                    >
                      <td>{{ item.title }}</td>
                      <td><a :href="item.file" download><v-icon color="primary">mdi-download-circle</v-icon></a></td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>        
            </v-card-text>
          </v-card>
        </v-tab-item>     
        <v-tab-item>
          <v-card>
            <v-card-text>
              <v-simple-table>
                <template v-slot:default>
                  <thead>
                    <tr>
                      <th class="text-left">
                        Наименование
                      </th>
                      <th class="text-left">
                        
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="item in razrDoc"
                      :key="item.name"
                    >
                      <td>{{ item.title }}</td>
                      <td><a :href="item.file" download><v-icon color="primary">mdi-download-circle</v-icon></a></td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>        
            </v-card-text>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card>
            <v-card-text>
              <h6>Приемная Председателя Правления </h6>
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-3">mdi-phone</v-icon>
                <a href="tel:+77182731201">+7 (7182) 73-12-01</a>
              </div>
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-3">mdi-email-edit</v-icon>
                <a href="mailto:info@caustic.kz"> info@caustic.kz</a>
              </div>

              <h6>Отдел кадров </h6>
              <div class="d-flex align-center my-2">
                <v-icon class="mr-3">mdi-phone</v-icon>
                <a href="tel: +7 (7182) 73-12-17"> +7 (7182) 73-12-17</a>
              </div>

              <h6>Канцелярия</h6>
              <div class="d-flex align-center my-2">
                <v-icon class="mr-3">mdi-phone</v-icon>
                <a href="tel: +7 (7182) 73-12-20"> +7 (7182) 73-12-20</a>
              </div>

              <p>
              140000, Республика Казахстан
              г. Павлодар, промышленная зона северная, строение 28/1 
              </p>     
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
      years: [
        {
          color: 'primary',
          year: '1962',
          text: 'разработано проектное задание на строительство Павлодарского химического комбината. Производственные мощности завода составили: по каустической соде — 120 тыс. тонн, по жидкому хлору — 90 тыс. тонн'
        },
        {
          color: 'primary',
          year: '1965',
          text: 'начато строительство Павлодарского химического завода'
        },
        {
          color: 'primary',
          year: '1991 ',
          text: 'Павлодарский химический завод занимает территорию 2 500 га, штат его сотрудников насчитывал 6 500 человек, включая 500 инженеров. Первая промышленная площадка Павлодарского химического завода состоит из 30 цехов и производит широкий спектр народно-хозяйственной продукции:  каустическая сода, хлор, гипохлорит натрия, хлорид аммония, присадки к смазочным маслам и моторные масла, флотационные реагенты (аэрофлоты), антифризы и антиобледенители, дезинфицирующие и отбеливающие средства, пластификаторы для пластмасс, фенолформальдегидную смолу, несколько видов пластиков и изделий из них. Эти продукты поставляются на промышленные предприятия Советского Союза, включая Казахстан, Россию, Беларусь, Узбекистан и Кыргызстан'
        },
        {
          color: 'primary',
          year: '1994–2002',
          text: 'производство на Павлодарском химическом заводе было остановлено. '
        },
        {
          color: 'primary',
          year: '2002',
          text: 'на базе Павлодарского химического завода создается Акционерное Общество «Каустик». В состав акционеров входят Акимат Павлодарской области и бывшие учредители Павлодарского химического завода'
        },
        {
          color: 'primary',
          year: '2010',
          text: 'АО «Каустик» завершает проектные работы и приступает к строительству нового производства каустической соды и хлорсодержащей продукции мембранным методом. Проект строительства завода подготовлен ТОО «КазГипроЦветМет» (Казахстан, г. Усть-Каменогорск), инжиниринг и поставка оборудования — Уденора С.п.А (Италия), монтаж — ТОО «СредАзЭнергоМонтаж» (Казахстан). Основные строительные работы завершены в 2010 году, а пуско-наладочные работы — в июле 2011 года. Тогда же был осуществлен пробный пуск завода. В октябре 2011 года начат выпуск товарной продукции: каустической соды, жидкого хлора, соляной кислоты и гипохлорита натрия.'
        },
        {
          color: 'secondary',
          year: '2013',
          text: 'АО «НАК «Казатомпром» вошло в состав  акционеров АО «Каустик». Сделка по приобретению акций АО «Каустик» осуществлена в рамках реализации поручения Президента Республики Казахстан Нурсултана Назарбаева по формированию полноценного химического кластера на базе свободной экономической зоны «Павлодар».'
        }
      ],
      corpDoc: [],
      razrDoc: []
    }),
    mounted() {
      axios
        .get('http://127.0.0.1:8000/api/v1/documents/')
        .then(response => (response.data.forEach(element => {
            console.log(element);
            if (element.type_of_file === "Корпоративные документы") {
              this.corpDoc.push(element)
            }else if (element.type_of_file === "Разрешительные документы") {
              console.log(element);
              this.razrDoc.push(element)
            }
          })))
        .catch(error => console.log(error));
    }
  }
</script>