<template>
    <md-content>
        <div class="categories">
            <section class="error" v-if="!categories">No categories found</section>
            <section id="category-list-container">
                <md-chip v-for="category in categories" :key="category"
                         @click="handleCategoryClick($event, category)"
                         md-clickable>{{category}}</md-chip>
            </section>
            <section>
                <md-button class="md-primary" :disabled="!categories" @click="handleRequest">Finish</md-button>
            </section>
        </div>
    </md-content>
</template>

<script>
    export default {
        name: "Categories",
        data () {
            return {
                selection: {},
                loading: false
            }
        },
        methods: {
            handleCategoryClick (event, category) {
                this.selection[category] = !this.selection[category];
                event.target.closest('.md-chip').classList.toggle('md-primary');
                this.$store.commit('updateCategorySelection', {
                    categories: this.categories.filter(category => this.selection[category])
                });
            },
            handleRequest () {
                this.$store.dispatch('postSurprise');
            }
        },
        computed: {
            categories () {
                return this.$store.state.surprise.categories;
            }
        },
        created () {
            this.$store.dispatch('getCategories');
        }
    }
</script>

<style lang="scss" scoped>
    .categories {
        display: flex;
        flex-direction: column;
    }

    #category-list-container {
        width: 24rem;
        display: flex;
        flex-wrap: wrap;
        align-self: center;
        .md-chip {
            margin: 0.5rem;
            &:hover {
                background-color: var(--md-theme-default-primary, #b71c1c);
                color: #fff;
                color: var(--md-theme-default-text-primary-on-primary, #fff);
            }
        }
    }
</style>