<template>
    <div id="p1">
        <el-tabs :tab-position="tabPosition" style="top:10%;height: 90%;">
            <el-tab-pane v-for="item in displays" :key="item.ref" :label="item.ref" style="height:100%">
                <ScaffoldVuer @scaffold-selected="onSelected" @on-ready="onReady" v-if="item.type === 'scaffold'" :url="item.url"
                              v-on:scaffold-selected="ScaffoldSelected" :ref="item.ref" style="height:100%" />
            </el-tab-pane>
        </el-tabs>

        <Teleport to="body">
            <modal :show="showModal" @close="showModal = false">
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
    import { ScaffoldVuer } from '@abi-software/scaffoldvuer';
    // Import other necessary components and libraries

    export default {
        name: 'page_01',
        components: {
            ScaffoldVuer,
            // Other components
        },
        data() {
            return {
                // Your data properties
            };
        },
        methods: {
            onReady() {
                this.$nextTick(() => {
                    const scene = this.$refs.scaffold.$module.scene;
                    const rootRegion = scene.getRootRegion();
                    const regions = rootRegion.getChildRegions();
                    regions.forEach(region => {
                        region.setVisibility(false);
                    });
                });
            },
            toggleRegionVisibility(region_name, visibility) {
                this.$nextTick(() => {
                    const scene = this.$refs.scaffold.$module.scene;
                    const rootRegion = scene.getRootRegion();
                    const region = rootRegion.getChildWithName(region_name);
                    if (region) {
                        region.setVisibility(visibility);
                    } else {
                        console.error(`Region with name ${region_name} not found.`);
                    }
                });
            },
            displayLabelWithGlyph() {
                // Implement logic to display labels with glyphs
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
