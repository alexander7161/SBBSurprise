# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Deployment to the Swisscom Application Cloud
You need to have the cloudfoundry-cli installed. https://docs.cloudfoundry.org/cf-cli/install-go-cli.html

Login to your developer console with your command-line:
```bash
cf login -a https://api.lyra-836.appcloud.swisscom.com -u <username>
```

Run:
```bash
cf push
```