<template>
  <div id="app">
    <nav class="nav">
      <router-link class="link" to="/">Skin Selection Tool</router-link>
      <router-link class="link" to="/Page-02">Heat Maps</router-link>
      
    </nav>
    <router-view/>
  </div>
</template>

<script>
import '@abi-software/scaffoldvuer/dist/scaffoldvuer.css';

export default {
  name: 'app',
}
</script>

<style>
body {
  margin: 0px; 
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
}

.nav {
  width: 100%;
  padding: 10px;
  background-color: #333;
}

.link {
  text-decoration: none;
  color: #fff;
  font-size: 14px;
  padding:  0px 10px;
  border-right: 1px solid #fff;
  transition: 0.5s ;
  color: #fff;
}

.link:last-child {
  border: none;
}

.link:hover {
  color: #ff9523;
}

</style>
