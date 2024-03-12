<template>
    <div id="p2">
        <el-tabs :tab-position="tabPosition" style="top:10%;height: 90%;">
            <el-tab-pane v-for="item in displays" :key="item.ref" :label="item.ref" style="height:100%">
                <ScaffoldVuer @on-ready="onReady" @scaffold-selected="offSelected" v-if="item.type === 'scaffold'" :url="item.url" v-on:scaffold-selected="ScaffoldSelected"
                              :ref="item.ref" style="height:100%" :checked="false" /> <!-- Pass the checked prop -->
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
    /* eslint-disable no-alert, no-console */
    import { ScaffoldVuer } from '@abi-software/scaffoldvuer';

    export default {
        name: 'Heat Maps',
        components: {
            ScaffoldVuer,
        },
        data: function () {
            return {
                tabPosition: 'left',
                selected: "Not Selected",
                displays: [
                    { type: 'scaffold', url: "/data/heat_maps.json" },
                   /* { type: 'scaffold', url: "/data/heat_maps_number_of_draining_nfs.json", ref: "Number of Draining NF Heat Maps" },
                   /* { type: 'scaffold', url: "/data/model2_metadata.json", ref: "Discrete Points" },*/
                ],
                scaffoldsArray: []
            }
        },
        methods: {
            onSelected: function (data) {
                console.log(data)
                alert("");
            },
            offSelected() {
                // Your logic for handling the 'offSelected' event
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

    #p2 {
        padding: 0;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        height: 100%;
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
</style>
