import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Reports from '@/components/information/Reports'
import Library from '@/components/facilities/Library'
import Admission from '@/components/academics/Admission'

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Home
    },
    {
      path: '/information/reports',
      name: 'Reports',
      component: Reports
    },
    {
      path: '/facilities/library',
      name: 'Library',
      component: Library
    },
    {
      path: '/academics/admission',
      name: 'Admission',
      component: Admission
    }
  ]
})
