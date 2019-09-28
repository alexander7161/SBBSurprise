<template>
    <div class="purchase">
        <md-card id="main-card">
            <md-card-header>
                <div class="md-title">Your surprise Roundtrip</div>
            </md-card-header>
            <md-card-content>
                <div class="datetime">{{ surprise.startDate }} {{ surprise.startTime }} - {{ surprise.endTime }}</div>
                <div class="startingpoint">{{ surprise.startLocation.name }}</div>
                <div class="price">{{ surprise.price }}</div>
                <md-button class="md-primary" @click="handleRequest">Buy Surprise</md-button>
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
            }
        },
        computed: {
            //Todo handle display if surprise is empty
            surprise() {
                return this.$store.state.surprise;
            }
        }

    }
</script>

<style scoped>
    #main-card {
        width: 48rem;
        padding-left: 5vw;
        padding-right: 5vw;
        margin-left: auto;
        margin-right: auto;
    }
</style>