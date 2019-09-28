<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
  @import "~vue-material/dist/theme/engine"; // Import the theme engine

  @include md-register-theme("default", (
  primary: md-get-palette-color(red, 900), // The primary color of your application
  accent: md-get-palette-color(blue, 200) // The accent or secondary color
  ));

  @import "~vue-material/dist/theme/all"; // Apply the theme

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
