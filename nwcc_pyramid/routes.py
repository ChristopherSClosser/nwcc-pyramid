"""NWCC routes."""


def includeme(config):
    """Defined routes."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('welcome', '/welcome')
    config.add_route('sundays', '/sundays')
    config.add_route('youth_kids', '/youth_kids')
    config.add_route('go_deeper', '/go_deeper')
    config.add_route('worship', '/worship')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('about', '/about_us')
    config.add_route('values', '/values')
    config.add_route('contact', '/contact')
    config.add_route('mission', '/mission_statement')
    config.add_route('staff', '/staff')
    config.add_route('council', '/council')
    config.add_route('beliefs', '/what_we_believe')
    config.add_route('im_new', '/im_new')
    config.add_route('foursquare', '/foursquare')
    config.add_route('giving', '/giving')
    config.add_route('events', '/events')
    config.add_route('foodbank', '/foodbank')
    config.add_route('connect', '/connect')
