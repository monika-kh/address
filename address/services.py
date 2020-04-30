from service_objects.services import Service

from .models import Block, District, State, Ward


class GetDisrtictService(Service):
    """
    Get list of district of a state.
    """

    def process(self):
        state_id = self.data.get("state_id")
        dist = District.objects.filter(state_id=state_id)
        return dist


class PostDistrictService(Service):
    """
    Create district for particular State_id.
    """

    def process(self):
        state_obj = State.objects.get(pk=self.data.get("state_id"))
        dist = District.objects.create(
            name=self.data.get("data")["name"],
            dis_code=self.data.get("data")["dis_code"],
            state=state_obj,
        )
        return dist


class DistrictDetailService(Service):
    """
    Get district by id of particular state.
    """

    def process(self):
        state_id = self.data["state_id"]
        dist_id = self.data["dist_id"]
        dist = District.objects.get(state_id=state_id, pk=dist_id)
        return dist


class UpdateDistService(Service):
    """
    Update district of particular state.
    """

    def process(self):
        state_id = self.data["state_id"]
        dist_id = self.data["dist_id"]
        dist_name = self.data.get("data")["name"]
        dist_code = self.data.get("data")["dis_code"]
        dis_update = District.objects.get(pk=dist_id, state=state_id)
        dis_update.name = dist_name
        dis_update.dis_code = dist_code
        dis_update.save()
        return dis_update


class DeleteDistrictService(Service):
    """
    Delete district of particular state by id.
    """

    def process(self):
        state_id = self.data.get("state_id")
        dist_id = self.data.get("dist_id")
        dist = District.objects.get(pk=dist_id, state=state_id)
        dist.delete()


class BlockListService(Service):
    """
    Get list of blocks of a district.
    """

    def process(self):
        # state_id = self.data['state_id']
        dist_id = self.data["dist_id"]
        block = Block.objects.filter(district=dist_id)
        return block


class CreateBlockService(Service):
    """
    Create new block for particular district.
    """

    def process(self):
        dist_id = self.data["dist_id"]
        dist = District.objects.get(pk=dist_id)
        block = Block.objects.create(
            name=self.data.get("data")["name"],
            block_code=self.data.get("data")["block_code"],
            district=dist,
        )
        return block


class BlockDetailService(Service):
    """
    Get block of by id of particular district.
    """

    def process(self):
        dist_id = self.data.get("dist_id")
        block_id = self.data.get("block_id")
        block = Block.objects.get(pk=block_id, district=dist_id)
        return block


class UpdateBlockService(Service):
    """
    Update block of particular district.
    """

    def process(self):
        dist_id = self.data.get("dist_id")
        block_id = self.data.get("block_id")
        block_name = self.data.get("data")["name"]
        block_code = self.data.get("data")["block_code"]

        update_block = Block.objects.get(pk=block_id, district=dist_id)

        update_block.name = block_name
        update_block.block_code = block_code
        update_block.save()
        return update_block


class DeleteBlockService(Service):
    """
    Delete block of particular district.
    """

    def process(self):
        block_id = self.data["block_id"]
        dist_id = self.data["dist_id"]
        block = Block.objects.get(pk=block_id, district=dist_id)
        block.delete()


class WardListService(Service):
    """
    Get List of wards of a block.
    """

    def process(self):
        # dist_id = self.data['dist_id']
        block_id = self.data["block_id"]
        ward = Ward.objects.filter(block_id=block_id)
        return ward


class CreateWardService(Service):
    """
    Create new ward for particular block.
    """

    def process(self):
        block_id = self.data.get("block_id")
        block_obj = Block.objects.get(pk=block_id)

        ward = Ward.objects.create(
            name=self.data.get("data")["name"],
            ward_code=self.data.get("data")["ward_code"],
            block=block_obj,
        )
        return ward


class WardDetailService(Service):
    """
    Get ward by id.
    """

    def process(self):
        ward_id = self.data.get("ward_id")
        block_id = self.data.get("block_id")
        ward = Ward.objects.get(pk=ward_id, block=block_id)
        return ward


class UpdateWardService(Service):
    def process(self):
        """
        Update ward of particular block.
        """
        block_id = self.data.get("block_id")
        ward_id = self.data.get("ward_id")
        update_name = self.data.get("data")["name"]
        update_ward_code = self.data.get("data")["ward_code"]
        ward = Ward.objects.get(pk=ward_id, block=block_id)
        ward.name = update_name
        ward.ward_code = update_ward_code
        ward.save()
        return ward


class DeleteWardService(Service):
    """
    Delete ward by id.
    """

    def process(self):
        block_id = self.data.get("block_id")
        ward_id = self.data.get("ward_id")
        ward = Ward.objects.get(pk=ward_id, block=block_id)
        ward.delete()
