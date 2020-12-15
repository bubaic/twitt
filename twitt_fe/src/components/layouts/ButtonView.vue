<template>
	<span v-for="role in roles" :key="role">
		<button :role="role" :class="role" @click="handleClick(role)">
			<span v-if="role === 'like'">{{ likes }}</span>
			{{ role }}
		</button>
		<span>&nbsp;</span>
	</span>
</template>

<script>
	export default {
		props: ["roles", "likes"],
		emits: ["handleAction"],
		methods: {
			handleClick: function(role) {
				this.$emit("handleAction", role);
			},
		},
	};
</script>

<style lang="scss">
	button {
		max-width: 200pt;
		font-size: 10pt;
		text-transform: uppercase;
		word-wrap: break-word;
		background: #1c1e26;
		margin-right: auto;
		font-weight: 600;
		outline: 0;
		border: 0;
		padding: 4pt 8pt;
		color: #ebebeb;
		border-radius: 3pt;

		&:hover {
			background: #474c61;
		}
	}
	.like {
		background: #4169e1;

		&:hover {
			background: lighten(#4161e1, 10%);
		}
	}
	.dislike {
		background: #dc143c;

		&:hover {
			background: lighten(#dc1c3c, 10%);
		}
	}
	.retweet {
		background: #5f9f3f;

		&:hover {
			background: lighten(#5f9f3f, 10%);
		}
	}
</style>
