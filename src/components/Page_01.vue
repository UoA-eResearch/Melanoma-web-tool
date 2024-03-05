<template>
    <div id="p1">
        <el-tabs :tab-position="tabPosition" style="top:10%;height: 90%;">
            <el-tab-pane v-for="item in displays" :key="item.ref" :label="item.ref" style="height:100%">
                <ScaffoldVuer @on-ready="onReady" @scaffold-selected="onSelected" v-if="item.type === 'scaffold'"
                    :url="item.url" v-on:scaffold-selected="ScaffoldSelected" :ref="item.ref" :style="{ 'margin-right': showSidebar ? sidebarWidth : '0', 'height': '100%' }" />
                <div v-show="showSidebar">
                    <div class="sidebar" :class="{ 'show': showSidebar }">
                        <button @click="showSidebar = false">Hide STATISTICS</button>
                        <h3 v-if="selectedElm">STATISTICS - {{ selectedElm }}</h3>
                        <table v-if="selectedElmData">
                            <thead>
                                <th class="right-align">Code</th>
                                <th>Nodefield</th>
                                <th class="right-align"># Cases</th>
                                <th class="right-align">Drainage Statistics</th>
                            </thead>
                            <tbody>
                                <tr v-for="elm in selectedElmData" v-bind:key="elm.id">
                                    <td class="right-align">{{ elm.code }}</td>
                                    <td>{{ elm.name }}</td>
                                    <td class="right-align">{{ elm.count }}</td>
                                    <td class="right-align">{{ elm.percentage }}</td>
                                </tr>
                            </tbody>
                        </table>
                        <span v-else>No data available!</span>
                    </div>
                </div>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
/* eslint-disable no-alert, no-console */
import { ScaffoldVuer } from '@abi-software/scaffoldvuer';
import data_elements from '@/data/data_elements.json';
export default {
    name: 'page_01',
    components: {
        ScaffoldVuer,
    },
    data: function () {
        return {
            showSidebar: false,
            sidebarWidth: '20%',
            tabPosition: 'left',
            selected: " Selected",
            displays: [


                { type: 'scaffold', url: "/data/all_element_jasons/element_all.json", ref: "Skin Selection Tool" },
                { type: 'scaffold', url: "/data/skin_cancer_metadata1.json", ref: "Skin Cancer" },
            ],
            scaffoldsArray: [],
            selectedElm: '',
            selectedElmData: [],
            data_elements: data_elements,
        }
    },
    methods: {
        onSelected: function (response) {
            const { data: { id } } = response?.[0];

            this.selectedElmData = this.data_elements[id];
            this.selectedElm = id;
            this.showSidebar = true;
            

            // Toggle region visibility
            this.displays.forEach(item => {
                if (this.$refs[item.ref] && this.$refs[item.ref].$module) {
                    const scene = this.$refs[item.ref].$module.scene;
                    const rootRegion = scene.getRootRegion();
                    const region = rootRegion.getChildWithName(this.selectedElm);
                    if (region) {
                        region.setVisibility(true); // or region.setVisibility(false)
                    }
                }
            });

        },
        ScaffoldSelected: function (annotation) {
            this.selected = annotation[0].data.id;
        },
        AddData: function () {
            if (this.csvFiles.length)
                this.displays.push(this.csvFiles.shift());
        },
        onReady() {
            console.log('zoom out');
            this.$refs['Skin Selection Tool'][0].$module.scene.viewAll();
            this.displays.forEach(item => {
                if (this.$refs[item.ref] && this.$refs[item.ref].$module) {
                const scene = this.$refs[item.ref].$module.scene;
                const rootRegion = scene.getRootRegion();
                const regions = rootRegion.getChildRegions();
                regions.forEach(region => {
                    region.setVisibility(false);
                });
            }
            });
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

.sidebar {
    position: fixed;
    right: 0;
    top: 50px;
    width: 20%;
    height: 60%;
    overflow: auto;
    background-color: #f5f5f5;
    padding: 20px;
    box-sizing: border-box;
    transition: transform 0.3s ease-in-out;
    transform: translateX(100%);
    border: 2px solid #007BFF; /* Add a border */
    border-radius: 10px; /* Rounded corners */
}

.sidebar.show {
    transform: translateX(0);
}

.sidebar h3 {
    color: #007BFF; /* Change the color of the header */
    border-bottom: 1px solid #007BFF; /* Add a bottom border to the header */
    padding-bottom: 10px; /* Add some padding to the bottom of the header */
}

.sidebar button {
    background-color: #007BFF; /* Change the background color of the button */
    color: #fff; /* Change the text color of the button */
    border: none; /* Remove the border of the button */
    padding: 10px 20px; /* Add some padding to the button */
    border-radius: 5px; /* Rounded corners for the button */
    cursor: pointer; /* Change the cursor when hovering over the button */
}

.sidebar button:hover {
    background-color: #0056b3; /* Change the background color of the button when hovering */
}

.sidebar table {
    width: 100%;
    border-collapse: collapse; /* Remove the space between the borders of the table and cells */
}
.sidebar th, .sidebar td {
    padding: 10px;
    border: 1px solid #ddd; /* Add a border to the cells */
    text-align: left; /* Align the text to the left */
}

.sidebar th {
    background-color: #007BFF; /* Change the background color of the header cells */
    color: #fff; /* Change the text color of the header cells */
}
.sidebar tr:hover {
    background-color: #53e45f; /* Add a background color to the table rows when hovering */
}
.sidebar tr{
    /* first letter capital */
    text-transform: capitalize;
    /* text alignment */
    text-align: center;
    /* font size */
    font-size: 1rem;
}
</style>