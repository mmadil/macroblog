;( function( window ) {
	
	'use strict';

	var docElem = window.document.documentElement;

	function getViewportH() {
		var client = docElem['clientHeight'],
			inner = window['innerHeight'];
		
		if( client < inner )
			return inner;
		else
			return client;
	}

	function scrollY() {
		return window.pageYOffset || docElem.scrollTop;
	}

	// http://stackoverflow.com/a/5598797/989439
	function getOffset( el ) {
		var offsetTop = 0, offsetLeft = 0;
		do {
			if ( !isNaN( el.offsetTop ) ) {
				offsetTop += el.offsetTop;
			}
			if ( !isNaN( el.offsetLeft ) ) {
				offsetLeft += el.offsetLeft;
			}
		} while( el = el.offsetParent )

		return {
			top : offsetTop,
			left : offsetLeft
		}
	}

	function inViewport( el, h ) {
		var elH = el.offsetHeight,
			scrolled = scrollY(),
			viewed = scrolled + getViewportH(),
			elTop = getOffset(el).top,
			elBottom = elTop + elH,
			h = h || 0;

		return (elTop + elH * h) <= viewed && (elBottom) >= scrolled;
	}

	function extend( a, b ) {
		for( var key in b ) { 
			if( b.hasOwnProperty( key ) ) {
				a[key] = b[key];
			}
		}
		return a;
	}

	function Scroller( el, options ) {	
		this.el = el;
		this.options = extend( this.defaults, options );
		this._init();
	}

	Scroller.prototype = {
		defaults : {
			viewportFactor : 0.2
		},
		_init : function() {
			if( Modernizr.touch ) return;
			this.sections = Array.prototype.slice.call( this.el.querySelectorAll( '.section' ) );
			this.didScroll = false;

			var self = this;
			// the sections already shown...
			this.sections.forEach( function( el, i ) {
				if( !inViewport( el ) ) {
					classie.add( el, 'scroll-side-init' );
				}
			} );

			var scrollHandler = function() {
					if( !self.didScroll ) {
						self.didScroll = true;
						setTimeout( function() { self._scrollPage(); }, 60 );
					}
				},
				resizeHandler = function() {
					function delayed() {
						self._scrollPage();
						self.resizeTimeout = null;
					}
					if ( self.resizeTimeout ) {
						clearTimeout( self.resizeTimeout );
					}
					self.resizeTimeout = setTimeout( delayed, 200 );
				};

			window.addEventListener( 'scroll', scrollHandler, false );
			window.addEventListener( 'resize', resizeHandler, false );
		},
		_scrollPage : function() {
			var self = this;

			this.sections.forEach( function( el, i ) {
				if( inViewport( el, self.options.viewportFactor ) ) {
					classie.add( el, 'section-animate' );
				}
				else {
					// this add class init if it doesn't have it. This will ensure that the items initially in the viewport will also animate on scroll
					classie.add( el, 'scroll-side-init' );
					
					classie.remove( el, 'section-animate' );
				}
			});
			this.didScroll = false;
		}
	}

	// add to global namespace
	window.Scroller = Scroller;

} )( window );

