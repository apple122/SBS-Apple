import server from '../API-links/server'
export default {
    Mainurl: server.Mainurl,

    getproveince: 'api/v1/province?is_active=true',
    getprobyID: 'api/v1/province/',
    createprovence: 'api/v1/province',
    putproveince: 'api/v1/province/',
    deleprovince: 'api/v1/province/',
    patchprovince: 'api/v1/province/',

    getdistrict: 'api/v1/district?depth=true&is_active=true',
    createdistric: 'api/v1/district',
    patchdistrict: 'api/v1/district/',
}