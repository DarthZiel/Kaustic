import VueRouter from 'vue-router'
import homeVue from '../components/home/homeVue'
import aboutVue from '../components/about/aboutVue'
import investVue from '../components/invest/investVue'
import ecologyVue from '../components/ecology/ecologyVue'
import careerVue from '../components/career/careerVue'
import serviceVue from '../components/service/serviceVue'
import newsVue from '../components/news/newsVue'
import projectsVue from '../components/projects/projectsVue'


export default new VueRouter ({
  routes: [
    {
      path: '',
      component: homeVue
    },
    {
      path: '/about',
      component: aboutVue
    },
    {
      path: '/invest',
      component: investVue
    },
    {
      path: '/ecology',
      component: ecologyVue
    },
    {
      path: '/career',
      component: careerVue
    },
    {
      path: '/service',
      component: serviceVue
    },
    {
      path: '/news',
      component: newsVue
    },
    {
      path: '/projects',
      component: projectsVue
    }
  ],
  mode: 'history' 
})