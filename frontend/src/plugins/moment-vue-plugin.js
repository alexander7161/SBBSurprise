import moment from 'moment';

const VueMoment = {
    install (Vue, options) {
        Object.defineProperty(Vue.prototype, '$moment', { value: moment });
    }
};

export default VueMoment;