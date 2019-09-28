<template>
    <div class="success">
        <md-card id="main-card">
            <md-card-header>
                <div class="md-title">Congratulations</div>
                <div class="md-subhead">You have successfully booked your surprise roundtrip.</div>
            </md-card-header>
        </md-card>
    </div>
</template>

<script>
    export default {
        name: "Success"
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