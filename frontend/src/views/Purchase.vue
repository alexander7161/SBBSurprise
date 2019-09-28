<template>
    <div class="purchase">
        <md-card id="main-card">
            <md-card-header>
                <div class="md-title">Your surprise Roundtrip</div>
            </md-card-header>
            <md-card-content>
                <div class="startingpoint">{{ surprise.startLocation.name }}</div>
                <div class="datetime">{{ surprise.startDate }} {{ surprise.startTime }} - {{ surprise.endTime }}</div>
                <div class="price">{{ surprise.price }}</div>
                <md-button class="md-primary md-raised buy" @click="handleRequest">Buy Surprise</md-button>
                <br/>
                <md-button class="md-primary" @click="showOptions">I don't like this option!</md-button>
            </md-card-content>
        </md-card>
    </div>
</template>

<script>
    import router from "../router";

    export default {
        name: "Purchase",
        components: {},
        methods: {
            handleRequest() {
                router.push({name: 'success'});
            },
            showOptions() {
                router.push({name: 'alternatives'})
            }
        },
        computed: {
            surprise() {
                return this.$store.state.surprise;
            }
        }

    }
</script>

<style scoped>
    #main-card {
        width: 48rem;
        max-width: 90%;
        padding-left: 5vw;
        padding-right: 5vw;
        margin-left: auto;
        margin-right: auto;
    }

    .buy {
        width: 50%;
        margin-bottom: 5%;
    }
</style>