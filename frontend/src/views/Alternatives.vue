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
                    <md-card v-for="offer in offers" class="surpriseCards">
                        <md-button class="surprise" @click="chooseSurprise(offer)">
                            <li>
                                {{ wizard.startLocation.name }} {{ wizard.startDate }} {{offer.startTime}} -
                                {{offer.endTime}} Price: {{offer.price}}
                            </li>
                        </md-button>
                    </md-card>
                </ul>
            </md-card-content>
        </md-card>
    </div>
</template>

<script>
    export default {
        name: "Alternatives",
        methods: {
            chooseSurprise(surprise) {
                this.$store.commit('setSurprise', surprise);
                this.$router.push({name: 'purchase'});
            }, showOptions() {
                //Todo enable Options like specific Time ranges (startTime and endTime),
                // a different end location (so no roundtripp), a maximum time one wants to stay in the trains,
                // exclude mobility options (not by boat - seasick, or by bus - wheelchair)
            }
        },
        computed: {
            wizard() {
                return this.$store.state.wizard;
            },
            offers() {
                return [...Array(this.$store.state.offers.length).keys()].map(num => this.$store.getters.getOffer(num))
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