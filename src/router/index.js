import Vue from 'vue'
import VueRouter from 'vue-router'
import Page01 from '../components/Page_01.vue';
import Page02 from '../components/Page_02.vue';
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Page 01',
      component: Page01
    },
    {
      path: '/Page-02',
      name: 'Page 02',
      component: Page02
    }
  ]
})

export default router
