<template>
    <md-app id="app">
        <md-app-toolbar class="md-primary">
            <button id="homebutton" class="md-title" @click="goHome">SBB Surprise</button>
        </md-app-toolbar>
        <md-app-content>
            <div id="loading-screen" v-if="loading">
                <img src="./assets/logoAnimation.gif" alt="Loading animation">
            </div>
            <router-view/>
        </md-app-content>
    </md-app>
</template>

<script>
    import router from "./router";

    export default {
        computed: {
            loading () {
                return this.$store.state.wizard.loading;
            }
        },
        methods: {
            goHome() {
                router.push({name: 'home'})
            }
        }
    }
</script>

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
        height: 100vh;
    }

    #loading-screen {
        z-index: 10;
        position: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: #595d90;
        > img {
            max-width: 35vw;
            display: block;
        }
        @media screen and (max-width: 556px) {
            > img {
                max-width: initial;
                width: inherit;
                object-fit: cover;
            }
        }
    }

    #homebutton {
        background: none;
        border: none;
    }

    #homebutton:hover {
        cursor: pointer;
    }
</style>
