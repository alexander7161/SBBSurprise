<template>
    <div class="categories">
        <div>
            <section class="error" v-if="!categories">No categories found</section>
            <section v-else>
                <div class="md-title">Pick categories of activities you might enjoy.</div>
            </section>
            <section id="category-list-container">
                <md-chip v-for="category in categories" :key="category"
                         @click="handleCategoryClick($event, category)"
                         md-clickable>{{category}}</md-chip>
            </section>
            <section>
                <md-button class="md-primary md-raised" :disabled="!categories" @click="handleRequest">
                    Surprise me
                </md-button>
            </section>
        </div>
    </div>
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
                event.target.closest('.md-chip').classList.toggle('md-selected');
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
        width: inherit;
        height: inherit;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        .md-button {
            margin-top: 1.5rem;
        }
    }

    #category-list-container {
        width: 24rem;
        display: flex;
        flex-wrap: wrap;
        align-self: center;
        justify-content: center;
        margin-top: 1.5rem;
        .md-chip {
            margin: 0.5rem;
            &.md-selected {
                background-color: var(--md-theme-default-icon, rgba(0, 0, 0, 0.54));
                color: #fff;
                color: var(--md-theme-default-text-primary-on-icon, #fff);
            }
        }
    }
</style>