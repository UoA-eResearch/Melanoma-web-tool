<script>


export default {
  
  props: {
    show: Boolean
  },
  data() {
    return {
      posX: 0,
      posY: 0,
      dragging: false
    };
  },
  directives: {
    draggable: {
      inserted(el, binding, vnode) {
        el.style.position = 'absolute';
        el.onmousedown = (e) => {
          vnode.context.dragging = true;
          let offsetX = e.clientX - el.getBoundingClientRect().left;
          let offsetY = e.clientY - el.getBoundingClientRect().top;

          function onMouseMove(e) {
            if (vnode.context.dragging) {
              vnode.context.posX = e.clientX - offsetX;
              vnode.context.posY = e.clientY - offsetY;
            }
          }

          function onMouseUp() {
            vnode.context.dragging = false;
            document.removeEventListener('mousemove', onMouseMove);
          }

          document.addEventListener('mousemove', onMouseMove);
          document.addEventListener('mouseup', onMouseUp);
        };

        el.ondragstart = () => false;
      }
    }
  },
  beforeDestroy() {
    document.removeEventListener('mousemove', this.onMouseMove);
    document.removeEventListener('mouseup', this.onMouseUp);
  },
  methods: {
    onMouseMove(e) {
      if (this.dragging) {
        this.posX = e.clientX - this.offsetX;
        this.posY = e.clientY - this.offsetY;
      }
    },
    onMouseUp() {
      this.dragging = false;
    }
  }
}
</script>

<template>

    <div v-draggable v-if="show" class="modal-container" :style="{ left: posX + 'px', top: posY + 'px' }">
      <div class="modal-header">
        <slot name="header">default header</slot>
      </div>

      <div class="modal-body">
        <slot name="body"></slot>
      </div>

      <div class="modal-footer">
        <slot name="footer">
          <button class="modal-default-button" @click="$emit('close')">Done</button>
        </slot>
      </div>
    </div>
</template>

<style>
.modal-container {
  width: 30%;
  margin: 45px 20px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  position: absolute;
  right: 0;
  top: 0;
  height: 40%;
  cursor: move;
}

.modal-header h3 {
  margin-top: 0;
  padding: 10px 20px;
  border-bottom: 1px solid #777;
  text-align: left;
}

.modal-body {
  text-align: left;
  padding: 0 20px;
  overflow-y: auto;
  /* Add scroll if necessary */
}

.modal-footer {
  padding: 20px;
}

.modal-default-button {
  float: right;

}

/* CSS */
.modal-default-button {
  appearance: none;
  background-color: #FAFBFC;
  border: 1px solid rgba(27, 31, 35, 0.15);
  border-radius: 6px;
  box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;
  box-sizing: border-box;
  color: #24292E;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  padding: 6px 16px;
  position: relative;
  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;
  word-wrap: break-word;
}

.modal-default-button:hover {
  background-color: #F3F4F6;
  text-decoration: none;
  transition-duration: 0.1s;
}

.modal-default-button:disabled {
  background-color: #FAFBFC;
  border-color: rgba(27, 31, 35, 0.15);
  color: #959DA5;
  cursor: default;
}

.modal-default-button:active {
  background-color: #EDEFF2;
  box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
  transition: none 0s;
}

.modal-default-button:focus {
  outline: 1px transparent;
}

.modal-default-button:before {
  display: none;
}

.modal-default-button:-webkit-details-marker {
  display: none;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>