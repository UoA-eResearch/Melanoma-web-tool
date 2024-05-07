<template>
    <div>
        <div id="p2">
            <el-tabs :tab-position="tabPosition" style="top:10%;height: 90%;">
                <el-tab-pane v-for="item in displays" :key="item.ref" :label="item.ref" style="height:100%">
                    <ScaffoldVuer @on-ready="onReady"   v-if="item.type === 'scaffold'" :url="item.url" 
                                  v-on:scaffold-selected="ScaffoldSelected" style="height:100%" :checked="false" ref="scaffold"/> <!-- Pass the checked prop -->
                </el-tab-pane>
            </el-tabs>
        </div>
        
    </div>
</template>



<script>
    /* eslint-disable no-alert, no-console */
    import { ScaffoldVuer } from '@abi-software/scaffoldvuer';

    export default {
        name: 'HeatMaps',
        components: {
            ScaffoldVuer,
        },
        data: function () {
            return {
                tabPosition: 'left',
                selected: "Not Selected",
                displays: [
                    /*{ type: 'scaffold', url: "/data/all_element_jasons/Alan/mouseLungs_metadata.json" },*/
                    { type: 'scaffold', url: "/data/heat_maps.json" },
                   /* { type: 'scaffold', url: "/data/model2_metadata.json", ref: "Discrete Points" },*/
                ],
                scaffoldsArray: [],
                
            }
        },
        methods: {
            
            /*onHighlighted: function () {
                console.log(this.$refs.scaffold)
                console.log(this.$refs['scaffold']) 
                this.$refs['scaffold'].objectHovered(undefined, false);
    },*/
            
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
            /*onReady() {
                console.log('zoom out');
                console.log(this.$refs['scaffold']);
                this.$refs['scaffold'][0].$module.scene.viewAll();

                // Using requestAnimationFrame to wait for the next repaint cycle
                requestAnimationFrame(() => {
                    console.log('DOM updated, unchecking checkboxes...');

                    const checkboxes = document.querySelectorAll('.el-tree-node input[type="checkbox"]');
                    console.log('Found checkboxes:', checkboxes);

                    // Optimize checkbox unchecking process
                    const checkboxesToUncheck = Array.from(checkboxes).slice(1); // Exclude the first checkbox
                    checkboxesToUncheck.forEach((checkbox, index) => {
                        checkbox.checked = false;
                        console.log(`Checkbox ${index + 2}: Unchecked`); // Adjust index since we start from the second checkbox
                    });
                });
            }
,*/





            onReady() {
                console.log('zoom out');
                if (this.$refs['scaffold']) {
                    console.log(this.$refs['scaffold']);

                    // Check if `$module` property exists before accessing `scene` property
                    if (this.$refs['scaffold'].$module && this.$refs['scaffold'].$module.scene) {
                        this.$refs['scaffold'].$module.scene.viewAll();
                    } 
                } 

                // Uncheck checkboxes
                const checkboxes = document.querySelectorAll('.el-tree-node input[type="checkbox"]');
                console.log('Found checkboxes:', checkboxes);

                // Uncheck all checkboxes except the first one
                for (let i = 0; i < checkboxes.length; i++) {
                    checkboxes[i].click(); // Trigger click event to uncheck
                    console.log(`Checkbox ${i + 1}: Unchecked`); // Adjust index since we start from the second checkbox
                }
                
            }
    
            
            
            },


        

           /* onReady() {
                console.log('zoom out');

                if (this.$refs['scaffold']) {
                    console.log(this.$refs['scaffold']);

                    // Check if `$module` property exists before accessing `scene` property
                    if (this.$refs['scaffold'].$module && this.$refs['scaffold'].$module.scene) {
                        this.$refs['scaffold'].$module.scene.viewAll();
                    } 
                } 

                console.log('zoom--out');
            }*/



            /*setRegionVisibilityWithDelay() {
                console.log('zoomout');
                if (this.$refs['scaffold']) {
                    console.log(this.$refs['scaffold']);

                    // Check if `$module` property exists before accessing `scene` property
                    if (this.$refs['scaffold'].$module && this.$refs['scaffold'].$module.scene) {
                        this.$refs['scaffold'].$module.scene.viewAll();
                    } 
                } 
                this.displays.forEach(item => {
                    if (this.$refs[item.$ref] && this.$refs[item.$ref].$module) {
                        const scene = this.$refs[item.$refs].$module.scene;
                        const rootRegion = scene.getRootRegion();
                        const regions = rootRegion.getChildRegions();
                        regions.forEach(region => {
                            // Check if the region name matches the desired name
                            if (region.getName() === "Left Axilla") {
                                setTimeout(() => {
                                    region.setVisibility(false);
                                }, 300); // Delay in milliseconds (adjust as needed)
                            }
                        });
                    }
                });
            }*/
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
