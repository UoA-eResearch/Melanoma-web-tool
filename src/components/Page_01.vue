<template>
    <div id="p1">
        <el-tabs :tab-position="tabPosition" style="top:10%;height: 90%;">
            <el-tab-pane v-for="item in displays" :key="item.ref" :label="item.ref" style="height:100%">
                <ScaffoldVuer @scaffold-selected="onSelected" v-if="item.type === 'scaffold'" :url="item.url"
                              v-on:scaffold-selected="ScaffoldSelected" :ref="item.ref" style="height:100%" />
            </el-tab-pane>
        </el-tabs>

        <Teleport to="body">
            <modal :show="showModal" @close="showModal = false">
                <template #header>
                    <h3>STATISTICS - {{selectedElm}}</h3>
                </template>
                <template #body>
                    <!-- Statistics Table -->
                </template>
            </modal>
        </Teleport>
        <span>{{testName}}</span>
    </div>
</template>

<script>
    import { ScaffoldVuer } from '@abi-software/scaffoldvuer';
    import Modal from './Modal.vue';
    import data_elements from '@/data/data_elements.json';

    export default {
        name: 'page_01',
        components: {
            ScaffoldVuer,
            Modal
        },
        data() {
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
                data_elements: data_elements
            }
        },
        methods: {
            onSelected(response) {
                const { data: { id } } = response?.[0];
                this.selectedElmData = this.data_elements[id];
                this.selectedElm = id;
                this.showModal = true;
            },
            ScaffoldSelected(annotation) {
                this.selected = annotation[0].data.id;
            },
            onReady() {
                const scene = this.$refs.scaffold.$module.scene;
                const rootRegion = scene.getRootRegion();
                const regions = rootRegion.getChildRegions();
                regions.forEach(region => {
                    region.setVisibility(false);
                });
            },
            // Other methods...
        },
        mounted() {
            this.$nextTick(() => {
                this.onReady();
            });
        }
    }
</script>

<style>
    /* Styles... */
</style>
