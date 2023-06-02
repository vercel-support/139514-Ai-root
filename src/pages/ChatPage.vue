<template>
  <q-page class="column items-center justify-evenly" padding>
    <div class="container" ref="containerRef">
      <q-chat-message v-for="{ id, role, content, stamp } in chatStore.history" :key="id" :name="roleToDisplayName[role]"
        :avatar="roleToAvatarLink[role]" :sent="role === 'user'" :stamp="dayjs(stamp).fromNow()" size="8">
        <ChatItem :content="content" />
      </q-chat-message>
    </div>
    <div class="chat-input">
        <q-input type="text" v-model="inputData" placeholder="Enter Your query" />
        <q-btn color="primary" @click="sendMessage(inputData)" icon="send" flat dense round />
    </div>
  </q-page>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch } from 'vue';
import { storeToRefs } from 'pinia';
import dayjs from 'dayjs';
import { useRouter } from 'vue-router';
import { useQuasar, scroll } from 'quasar'
import axios from 'axios'; // Import Axios
import { QInput, QBtn } from 'quasar';
import { useAssistantStore } from '../stores/assistant';
import { useChatStore } from '../stores/chat';
import ChatItem from '../components/ChatItem.vue';
import { useCredentialStore } from '../stores/credential';
import { Message } from 'postcss';
const inputData = ''; 
const $q = useQuasar()
const router = useRouter();
const assistantStore = useAssistantStore();
const chatStore = useChatStore();
const credentialStore = useCredentialStore();
const { lastHistoryItem, deciding, thinking, executing } = storeToRefs(chatStore);
const roleToDisplayName = {
  user: 'ME',
  system: 'LeckyAI',
  assistant: assistantStore.name,
}
const roleToAvatarLink = {
  user: 'src/pages/user.jpg',
  system: 'src/pages/system.jpg',
  assistant: 'https://cdn.quasar.dev/img/avatar3.jpg',
}
const moveOn = async () => {
  deciding.value = false;
}
onMounted(async () => {
  scrollToBottom();
  try {
    if (lastHistoryItem.value?.role && ['user', 'system'].includes(lastHistoryItem.value?.role)) {
      await chatStore.chat();
    }
  } catch (e) {
    if (e instanceof Error) {
      $q.notify({
        type: 'negative',
        message: e.message,
      });
      return;
    }
    $q.notify({
      type: 'negative',
      message: `Unknown error: ${e}`,
    });
  }

})
const containerRef = ref<HTMLDivElement | null>(null);
const scrollToBottom = () => {
  if (containerRef.value) {
    const target = scroll.getScrollTarget(containerRef.value);
    const offset = containerRef.value.scrollHeight;
    const duration = 1000;
    scroll.animVerticalScrollTo(target, offset, duration);
  }
}
watch(chatStore, () => {
  scrollToBottom();
}, {
  deep: true
});
const sendMessage = async (inputData: string) => {
  try {
    if (inputData) {
    chatStore.history.push({
    role: 'user',
    content: inputData,
    id:    dayjs().toISOString(),
    stamp: dayjs().toISOString(),
    });
    }
    const response = await axios.post<Message>('api/index.py', {
      message:inputData,
    });
    const chatResponse = response.data;
    // Update the chatStore with the response
    chatStore.history.push({
    role: 'system',
    content: chatResponse.response,
    id: dayjs().toISOString(),
    stamp: dayjs().toISOString(),
  });
 
  } catch (error) {
    console.log(error);
  }
};
</script>

<style scoped lang="scss">
.container {
  @media screen and (max-width: 1024px) {
    width: 100%;
  }

  width: 80%;
}
.chat-input {
  position: relative;
  bottom: 10px;
  width: 100%; 
}
</style>
