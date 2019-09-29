<template>
    <div class="home">
        <md-card id="main-card">
            <md-card-header>
                <div class="md-title">Let us surprise you</div>
                <div class="md-subhead">Choose a starting point and a start date</div>
            </md-card-header>
            <md-card-content>
                <form>
                    <md-autocomplete required
                                     v-model="selectedStation.name"
                                     :md-options="stations"
                                     @md-changed="getStations"
                                     @md-opened="getStations"
                                     @md-selected="updateSelection">
                        <label>Station</label>

                        <template slot="md-autocomplete-item" slot-scope="{ item }">{{ item.dst_bezeichnung_offiziell
                            }}
                        </template>
                    </md-autocomplete>

                    <md-datepicker v-model="selectedDate" :md-disabled-dates="filterDate" />

                    <md-button class="md-primary md-raised" @click="handleRequest">Let's Go</md-button>
                </form>
            </md-card-content>
        </md-card>
    </div>
</template>

<script>
    export default {
        name: 'home',
        components: {},
        data() {
            return {
                showErrors: false,
                selectedStation: {
                    id: null,
                    name: null
                },
                selectedDate: null,
                stations: []
            }
        },
        methods: {
            getStations(query) {
                if (!query) return [];
                this.stations = new Promise(resolve => {
                    setTimeout(async () => {
                        const result = await fetch('https://data.sbb.ch/api/records/1.0/search/?dataset=betriebspunkte-didok' +
                            `&q=dst_bezeichnung_offiziell%3A+${query}&rows=20&sort=-didok85&facet=dst_abk&facet=nummer&facet=haltestelle` +
                            '&facet=didok&facet=land&refine.haltestelle=*&refine.land=Switzerland');
                        const data = await result.json();
                        resolve(data.records.map(record => record.fields));
                    }, 300)
                })
            },
            updateSelection(item) {
                this.selectedStation.id = item.didok85;
                this.selectedStation.name = item.dst_bezeichnung_offiziell;
            },
            filterDate (date) {
                const now = this.$moment();
                const then = this.$moment(date);
                return then.isBefore(now) || (then.isSame(now, 'day') && now.hour >= 17);
            },
            handleRequest() {
                if (!this.selectedStation || !this.selectedDate) {
                    // TODO: visualise errors
                    this.showErrors = true;
                    return;
                }
                this.showErrors = false;

                this.$store.commit('updateLocation', {
                    startLocation: this.selectedStation
                });

                this.$store.commit('updateDate', {
                    startDate: this.selectedDate.toISOString().slice(0, 10)
                });

                this.$router.push('categories');
            }
        },
        computed: {}
    }
</script>

<style lang="scss" scoped>
    .home {
        width: inherit;
        height: inherit;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    #main-card {
        width: 48rem;
        max-width: 90%;
        padding-left: 5vw;
        padding-right: 5vw;
        margin-left: auto;
        margin-right: auto;
    }
</style>
