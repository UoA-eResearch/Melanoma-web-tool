import Vue from 'vue';
import App from './App.vue';
import router from './router'
import '@tehsurfer/csvvuer'
import { Button, Tabs, TabPane } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(Button);
Vue.component(Tabs.name, Tabs);
Vue.component(TabPane.name, TabPane);

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
