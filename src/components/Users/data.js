import server from '../API-links/server'
export default {
    Mainurl: server.Mainurl,

    getusers: 'api/v1/user?is_staff=true',
    poostusers: 'api/v1/user/register_staff',
    patchusers: 'api/v1/user/',

    resetpassword: 'api/v1/reset/',
}