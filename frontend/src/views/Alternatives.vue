<template>
    <div class="alternative">
        <md-card id="main-card">
            <md-card-header>
                <div class="md-title">Alternatives</div>
                <div class="md-subhead">Click on an alternative Surprise Trip to choose it. <br/>If you need some
                    additional adjustments
                    click here:
                    <md-button id="options" class="md-primary" @click="showOptions">Options</md-button>
                </div>
            </md-card-header>
            <md-card-content>
                <ul id="surprises">
                    <md-card v-for="surprise in surprises" class="surpriseCards">
                        <md-button class="surprise" @click="chooseSurprise(surprise)">
                            <li>
                                {{ surprise.startLocation.name }} {{ surprise.startDate }} {{surprise.startTime}} -
                                {{surprise.endTime}} Price: {{surprise.price}}
                            </li>
                        </md-button>
                    </md-card>
                </ul>
            </md-card-content>
        </md-card>
    </div>
</template>

<script>
    import router from "../router";

    export default {
        name: "Alternatives",
        methods: {
            chooseSurprise(surprise) {
                this.saveChosenSurprise(surprise);
                router.push({name: 'purchase'});
            },
            saveChosenSurprise(surprise) {
                this.$store.commit('updateLocation', {
                    startLocation: surprise.startLocation
                });
                this.$store.commit('updateDate', {
                    startDate: surprise.startDate
                });
                this.$store.commit('updateStartTime', {
                    startTime: surprise.startTime
                });
                this.$store.commit('updateEndTime', {
                    endTime: surprise.endTime
                });
                this.$store.commit('updatePrice', {
                    price: surprise.price
                });
            }, showOptions() {
                //Todo enable Options like specific Time ranges (startTime and endTime),
                // a different end location (so no roundtripp), a maximum time one wants to stay in the trains,
                // exclude mobility options (not by boat - seasick, or by bus - wheelchair)
            }
        },
        computed: {
            surprises() {
                return this.$store.state.surprises;
            }
        }
    }
</script>

<style scoped>
    li {
        list-style: none;
    }

    ul {
        padding: 0;
    }

    .md-button {
        margin: 6px 0px;
    }

    #surprises button {
        cursor: pointer; /* Pointer/hand icon */
        width: 100%; /* Set a width if needed */
        display: block; /* Make the buttons appear below each other */
    }

    #surprises button:not(:last-child) {
        border-bottom: none; /* Prevent double borders */
    }

    .surpriseCards {
        width: 50%;
        margin: auto;
    }

    #options {
        vertical-align: middle;
    }
</style>