<template>
	<svg
		:viewbox="viewbox"
		:width="width + '%'"
		:style="svg"
		preserveAspectRatio="xMidYMid meet"
	>
		<rect
			x="0"
			y="0"
			:width="width + '%'"
			:height="height"
			:style="rect.style"
			:clip-path="rect.clipPath"
		/>
		<defs>
			<clipPath :id="clipPathID">
				<slot>
					<circle r="35" cx="35" cy="35" />
					<rect x="80" y="17" rx="4" ry="4" width="25%" height="15" />
					<rect x="80%" y="17" rx="4" ry="4" width="10%" height="12" />
					<circle r="8" cx="96%" cy="23" />
					<rect x="80" y="40" rx="3" ry="3" width="20%" height="10" />
					<rect x="0" y="80" rx="3" ry="3" width="100%" height="12" />
					<rect x="0" y="100" rx="3" ry="3" width="60" height="20" />
					<rect x="70" y="100" rx="3" ry="3" width="60" height="20" />
					<rect x="140" y="100" rx="3" ry="3" width="60" height="20" />
				</slot>
			</clipPath>

			<linearGradient :id="gradientID">
				<stop offset="0%" :stop-color="primary">
					<animate
						attributeName="offset"
						values="-2; 1"
						:dur="duration"
						repeatCount="indefinite"
					/>
				</stop>
				<stop offset="50%" :stop-color="secondary">
					<animate
						attributeName="offset"
						values="-1.5; 1.5"
						:dur="duration"
						repeatCount="indefinite"
					/>
				</stop>
				<stop offset="100%" :stop-color="primary">
					<animate
						attributeName="offset"
						values="-1; 2"
						:dur="duration"
						repeatCount="indefinite"
					/>
				</stop>
			</linearGradient>
		</defs>
	</svg>
</template>

<script>
	const colorValidator = (color) =>
		/^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$/.test(color);

	export default {
		name: "LoaderView",
		props: {
			rtl: { default: false, type: Boolean },
			speed: { default: 3, type: Number },
			width: { default: 100, type: Number },
			height: { default: 120, type: Number },
			primary: {
				default: "#f0f0f0",
				type: String,
				validator: colorValidator,
			},
			secondary: {
				default: "#e0e0e0",
				type: String,
				validator: colorValidator,
			},
		},
		computed: {
			_uid: function() {
				return btoa(Math.random()).substring(0, 12);
			},
			viewbox: function() {
				return `0 0 ${this.width} ${this.height}`;
			},
			gradientID: function() {
				return `gradient-${this._uid}`;
			},
			clipPathID: function() {
				return `clipPath-${this._uid}`;
			},
			svg: function() {
				if (this.rtl) {
					return { transform: "rotateY(180deg)" };
				}
			},
			rect: function() {
				return {
					style: { fill: "url(#" + this.gradientID + ")" },
					clipPath: "url(#" + this.clipPathID + ")",
				};
			},
			circle: function() {
				return {
					style: { fill: "url(#" + this.gradientID + ")" },
					clipPath: "url(#" + this.clipPathID + ")",
				};
			},
			duration: function() {
				return `${this.speed}s`;
			},
		},
	};
</script>

<style></style>
