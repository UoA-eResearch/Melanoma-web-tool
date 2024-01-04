<template>
  <div id="p1">
    <el-tabs :tab-position="tabPosition" style="top:10%;height: 90%;">
      <el-tab-pane v-for="item in displays" :key="item.ref" :label="item.ref" style="height:100%">
        <ScaffoldVuer @scaffold-selected="onSelected" v-if="item.type === 'scaffold'" :url="item.url"
          v-on:scaffold-selected="ScaffoldSelected" :ref="item.ref" style="height:100%" />
      </el-tab-pane>
    </el-tabs>

    <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @close="showModal = false">
      <!-- <template #header>
        <h3>Sample Header</h3>
      </template>
      <template #body>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Est sit amet facilisis magna etiam tempor orci. Augue eget arcu dictum varius duis. Rhoncus urna neque viverra justo nec ultrices dui. Et egestas quis ipsum suspendisse ultrices gravida. Elit ut aliquam purus sit amet luctus venenatis lectus magna. Nisl nunc mi ipsum faucibus. Ultrices eros in cursus turpis massa tincidunt dui ut. Turpis egestas pretium aenean pharetra magna ac placerat. Dictum sit amet justo donec enim diam vulputate. Netus et malesuada fames ac. Urna condimentum mattis pellentesque id nibh tortor id aliquet. Dolor magna eget est lorem. Dui id ornare arcu odio ut sem. Ipsum dolor sit amet consectetur. Orci sagittis eu volutpat odio facilisis mauris sit.
        </p>
      </template> -->
      <template #header>
        <h3>STATISTICS - {{selectedElm}}</h3>
      </template>
      <template #body>
        <table v-if="selectedElmData">
          <thead>
            <th class="right-align">Code</th>
            <th>Nodefield</th>
            <th class="right-align"># Cases</th>
            <th class="right-align">Drainage</th>
          </thead>
          <tbody>
            <tr v-for="elm in selectedElmData" v-bind:key="elm.id">
              <td class="right-align">{{elm.code}}</td>
              <td>{{elm.name}}</td>
              <td class="right-align">{{elm.count}}</td>
              <td class="right-align">{{elm.percentage}}</td>
            </tr>
          </tbody>
        </table>
        <span v-else>No data available!</span>
      </template>
    </modal>
  </Teleport>
  <span>{{testName}}</span>
  </div>
</template>

<script>
/* eslint-disable no-alert, no-console */
import { ScaffoldVuer } from '@abi-software/scaffoldvuer';
import Modal from './Modal.vue';

export default {
  name: 'page_01',
  components: {
    ScaffoldVuer,
    Modal
  },
  data: function () {
    return {
      showModal: false,
      tabPosition: 'left',
      selected: " Selected",
      displays: [


        { type: 'scaffold', url: "/data/all_element_jasons/element_all.json", ref: "Skin Selection Tool" },
        { type: 'scaffold', url: "/data/skin_cancer_metadata1.json", ref: "Skin Cancer" },
      ],
      scaffoldsArray: [],
      selectedElm: '',
      selectedElmData: [],
      data_elements: {
        "element_1090":[
            {
              "code":"lprea",
              "name":"Left Preauricular",
              "count":2,
              "percentage":66.7
            },
            {
              "code":"la",
              "name":"Left axilla",
              "count":20,
              "percentage":96.7
            },
            {
              "code":"lprea",
              "name":"Left Preauricular",
              "count":2,
              "percentage":66.7
            },
            {
              "code":"la",
              "name":"Left axilla",
              "count":20,
              "percentage":96.7
            },
            {
              "code":"lprea",
              "name":"Left Preauricular",
              "count":2,
              "percentage":66.7
            },
            {
              "code":"la",
              "name":"Left axilla",
              "count":20,
              "percentage":96.7
            },
            {
              "code":"lprea",
              "name":"Left Preauricular",
              "count":2,
              "percentage":66.7
            },
            {
              "code":"la",
              "name":"Left axilla",
              "count":20,
              "percentage":96.7
            },
            {
              "code":"lprea",
              "name":"Left Preauricular",
              "count":2,
              "percentage":66.7
            },
            {
              "code":"la",
              "name":"Left axilla",
              "count":20,
              "percentage":96.7
            }
        ]
      }
    }
  },
  methods: {
    onSelected: function (response) {
      const { data: { id } } = response?.[0];
      
      this.selectedElmData = this.data_elements[id];
      this.selectedElm = id;
      this.showModal = true;

    },
    RemoveModel: function () {
      var currentLength = this.displays.length;
      if (currentLength > 0)
        var removed = this.displays.shift()
      if (removed.type === 'scaffold') {
        this.scaffoldsArray.unshift(removed)
      }
      else if (removed.type === 'plot') {
        this.csvFiles.unshift(removed)
      }

    },
    ScaffoldSelected: function (annotation) {
      this.selected = annotation[0].data.id;
    },
    AddModel: function () {
      if (this.scaffoldsArray.length)
        this.displays.push(this.scaffoldsArray.shift());
    },
    AddData: function () {
      if (this.csvFiles.length)
        this.displays.push(this.csvFiles.shift());
    }
  }
}
</script>

<style>
body {
  margin: 0px
}

#p1 {
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  width: 100%;
  position: absolute;
}

.top-panel {
  padding: 1%;
  height: 4%;
}

.my-button {
  margin: 5px;
}

.el-tabs__content {
  height: 100%;
}

table {
  width: 100%;
  margin: 20px auto;
  table-layout: auto;
}

.fixed {
  table-layout: fixed;
}

table,
td,
th {
  border-collapse: collapse;
}

th,
td {
  padding: 10px;
  border: solid 1px;
  text-align: center;
}

.left-align {
  text-align: left;
}

.right-align {
  text-align: right;
}
</style>