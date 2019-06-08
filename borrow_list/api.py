from rest_framework import routers
from rental import api_views as rental_apis

router = routers.DefaultRouter()
router.register(r'friends', rental_apis.FriendViewset)
router.register(r'belongings', rental_apis.BelongingViewset)
router.register(r'borrowings', rental_apis.BorrowedViewset)
